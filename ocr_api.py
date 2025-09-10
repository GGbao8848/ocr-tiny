#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR-Tiny API服务
提供Web接口让其他机器可以访问本机的OCR功能
"""
import os
import cv2
from flask import Flask, request, jsonify
from ocr_tiny import ONNXPaddleOcr

# 创建Flask应用实例
app = Flask(__name__)

# 初始化OCR模型，只在应用启动时初始化一次
ocr = ONNXPaddleOcr(
    det_model_dir='./models/ppocrv5/det/det.onnx',
    rec_model_dir='./models/ppocrv5/rec/rec.onnx',
    cls_model_dir='./models/ppocrv5/cls/cls.onnx',
    use_angle_cls=True,
    use_gpu=False  # 如果使用GPU加速
)

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    """执行OCR识别的API端点
    接收POST请求，参数为图片路径，返回OCR识别结果
    """
    try:
        # 获取请求参数中的图片路径
        data = request.get_json()
        if not data or 'image_path' not in data:
            return jsonify({'error': '请提供图片路径参数 image_path'}), 400
            
        image_path = data['image_path']
        
        # 检查图片文件是否存在
        if not os.path.exists(image_path):
            return jsonify({'error': f'图片文件不存在: {image_path}'}), 404
            
        # 加载图片并执行OCR识别
        img = cv2.imread(image_path)
        if img is None:
            return jsonify({'error': f'无法读取图片文件: {image_path}'}), 400
            
        result = ocr.ocr(img, cls=True)
        
        # 处理识别结果，转换为更易读的格式
        formatted_result = []
        if result and len(result) > 0:
            for item in result[0]:
                formatted_result.append({
                    'coordinates': item[0],  # 文本区域坐标
                    'text': item[1][0],       # 识别的文本内容
                    # 'confidence': item[1][1]  # 置信度
                })
                
        # 返回识别结果
        return jsonify({
            'success': True,
            'image_path': image_path,
            'results': formatted_result,
            # 'total_text_regions': len(formatted_result)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    """API首页，提供简单的使用说明"""
    return jsonify({
        'service': 'OCR-Tiny API',
        'version': '1.0',
        'endpoint': '/ocr',
        'method': 'POST',
        'example': {
            'url': 'http://192.168.2.26:8848/ocr',
            'body': '{"image_path": "/path/to/image.jpg"}'
        }
    })

if __name__ == '__main__':
    # 启动Flask应用，监听在所有接口的8848端口
    app.run(host='0.0.0.0', port=8848, debug=False)


# curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/home/qzq/图片/Snipaste_2025-09-02_21-11-42.png"}' http://192.168.2.26:8848/ocr

# curl -X POST -H "Content-Type: application/json" -d '{"image_path": "/media/qzq/4t/AAA_myproject/ocr-tiny/images/Image01004_01.jpg"}' http://192.168.2.26:8848/ocr