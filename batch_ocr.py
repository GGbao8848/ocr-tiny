#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR-Tiny 批量处理脚本
演示如何对文件夹中的所有图像进行OCR检测
"""
import os
import cv2
import glob
from ocr_tiny import ONNXPaddleOcr
from ocr_tiny.onnx_paddleocr import sav2Img
from ocr_tiny.utils import draw_ocr
import time


def batch_ocr_folder(folder_path, output_folder=None, use_gpu=False):
    """
    批量处理文件夹中的所有图像
    
    参数:
        folder_path: 包含图像的文件夹路径
        output_folder: 输出结果的文件夹路径，默认为None（不保存图像结果）
        use_gpu: 是否使用GPU加速
    """
    # 初始化OCR模型
    ocr = ONNXPaddleOcr(
        det_model_dir='./models/ppocrv5/det/det.onnx',
        rec_model_dir='./models/ppocrv5/rec/rec.onnx',
        cls_model_dir='./models/ppocrv5/cls/cls.onnx',
        use_angle_cls=True,
        use_gpu=use_gpu
    )
    
    # 创建输出文件夹（如果指定）
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取文件夹中的所有图像文件
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tif', '*.tiff']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))
        image_files.extend(glob.glob(os.path.join(folder_path, ext.upper())))
    
    print(f"找到 {len(image_files)} 张图像待处理")
    
    # 遍历并处理每张图像
    total_time = 0
    for i, img_path in enumerate(image_files):
        try:
            # 加载图像
            img = cv2.imread(img_path)
            if img is None:
                print(f"警告: 无法加载图像 {img_path}")
                continue
            
            # 执行OCR识别
            s = time.time()
            result = ocr.ocr(img, cls=True)
            
            e = time.time()
            total_time += (e - s)
            
            # 打印识别结果
            print(f"\n第 {i+1}/{len(image_files)} 张图像: {os.path.basename(img_path)}")
            if result and len(result) > 0:
                print(f"检测到 {len(result[0])} 个文本块")
                for j, part in enumerate(result[0]):
                    print(f"  第{j+1}个文本块: {part[1]}")
                
                # 修改 sav2Img 调用，提供完整路径和唯一文件名
                if output_folder:
                    # 获取原始文件名（不含扩展名）
                    base_name = os.path.splitext(os.path.basename(img_path))[0]
                    # 构造完整的保存路径
                    save_path = os.path.join(output_folder, f"{base_name}_ocr_result.jpg")
                    sav2Img(img, result, name=save_path)
                
            else:
                print(f"  未检测到文本")
                
        except Exception as e:
            print(f"处理 {img_path} 时出错: {str(e)}")
    
    # 打印总体统计信息
    if len(image_files) > 0:
        avg_time = total_time / len(image_files)
        print(f"\n批量处理完成！")
        print(f"总共处理: {len(image_files)} 张图像")
        print(f"总耗时: {total_time:.3f} 秒")
        print(f"平均每张图像耗时: {avg_time:.3f} 秒")


if __name__ == '__main__':
    # 示例用法
    input_folder = '/home/qzq/下载/OCR_sample/images'  # 输入图像文件夹
    output_folder = '/home/qzq/下载/OCR_sample/images_ocr_results'  # 输出结果文件夹
    
    batch_ocr_folder(input_folder, output_folder, use_gpu=False)