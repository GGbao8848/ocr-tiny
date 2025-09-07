#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR-Tiny 测试脚本
用于验证ocr-tiny包的基本功能是否正常工作
"""
import os
import sys

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ocr_tiny import ONNXPaddleOcr


def test_ocr_tiny():
    print("开始测试OCR-Tiny包...")
    
    try:
        # 初始化OCR模型（使用CPU模式进行测试）
        print("初始化OCR模型...")
        ocr = ONNXPaddleOcr(
            det_model_dir='./models/ppocrv5/det/det.onnx',
            rec_model_dir='./models/ppocrv5/rec/rec.onnx',
            cls_model_dir='./models/ppocrv5/cls/cls.onnx',
            rec_char_dict_path='./models/ppocrv5/ppocrv5_dict.txt',
            use_angle_cls=True,
            use_gpu=False
        )
        print("OCR模型初始化成功!")
        
        # 检查模型文件是否存在
        if not os.path.exists('./models/ppocrv5/det/det.onnx'):
            print("警告: 检测模型文件不存在")
        if not os.path.exists('./models/ppocrv5/rec/rec.onnx'):
            print("警告: 识别模型文件不存在")
        if not os.path.exists('./models/ppocrv5/cls/cls.onnx'):
            print("警告: 分类模型文件不存在")
        if not os.path.exists('./models/ppocrv5/ppocrv5_dict.txt'):
            print("警告: 字典文件不存在")
        
        print("OCR-Tiny包测试完成!")
        print("\n使用说明:")
        print("1. 确保所有模型文件都已正确放置在models目录下")
        print("2. 运行example.py文件进行完整的OCR识别演示")
        print("3. 或在您的代码中导入ONNXPaddleOcr类进行使用")
        
    except Exception as e:
        print(f"测试失败: {str(e)}")
        print("请检查以下内容:")
        print("1. 是否已安装所有依赖包 (pip install -r requirements.txt)")
        print("2. 模型文件路径是否正确")
        print("3. 模型文件是否完整")


if __name__ == '__main__':
    test_ocr_tiny()