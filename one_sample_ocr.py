#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR-Tiny 示例脚本
演示如何使用OCR-Tiny包进行文本识别
"""
import os
import time
import cv2
from ocr_tiny import ONNXPaddleOcr
from ocr_tiny.utils import draw_ocr
from ocr_tiny.onnx_paddleocr import sav2Img


if __name__ == '__main__':
    
    # 初始化OCR模型
    ocr = ONNXPaddleOcr(
        det_model_dir='./models/ppocrv5/det/det.onnx',
        rec_model_dir='./models/ppocrv5/rec/rec.onnx',
        cls_model_dir='./models/ppocrv5/cls/cls.onnx',
        use_angle_cls=True,
        use_gpu=False  # 如果使用GPU加速
    )
    
    # 加载图像
    img_path = 'images/Image00186_01.tif'
    img = cv2.imread(img_path)
    
    # 执行OCR识别
    result = ocr.ocr(img, cls=True)
    
    # 打印识别结果的详细结构
    # print("\nOCR结果的详细结构:")
    # print(f"结果类型: {type(result)}")
    # print(f"图片数量: {len(result[0])}")

    print(result)

    # if result and len(result) > 0:
    #     # print(f"\n第一张图片数据类型: {type(result[0])}")
    #     print(f"第一张图片结果: {len(result[0])}")
    #     for j, part in enumerate(result[0]):
    #         # print(f"  第{j+1}部分类型: {type(part)}")
    #         # print(f"  坐标: {part[0]}")
    #         print(f"  第{j+1}部分内容: {part[1]}")
    # else:
    #     print("未检测到文本")