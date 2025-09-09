# OCR-Tiny

OCR-Tiny 是一个轻量级的光学字符识别（OCR）工具包，基于 ONNX 运行时和 PaddleOCR 模型，提供高效、准确的文本检测和识别能力。

## 项目简介
OCR-Tiny 旨在提供一个简单易用、高性能的OCR解决方案，适用于需要从图像中提取文本信息的各类场景。

## 项目优势
- **轻量级**：依赖库少，安装简单
- **高性能**：基于 ONNX 运行时，支持 CPU 和 GPU 推理
- **准确性**：使用 PaddleOCR v5 模型，提供高质量的文本检测和识别
- **易用性**：API 设计简洁明了，便于集成到其他项目

## 环境要求
- Python 3.7+ 环境
- 主要依赖库：
  - onnxruntime>=1.14.0：ONNX 模型运行时
  - opencv-python>=4.7.0：图像处理
  - numpy>=1.24.0：数值计算

## 安装依赖
```bash
pip install -r requirements.txt
```

## 基本用法
```python
import cv2
from ocr_tiny import ONNXPaddleOcr

# 初始化 OCR 模型
ocr = ONNXPaddleOcr(
    det_model_dir='./models/ppocrv5/det/det.onnx',
    rec_model_dir='./models/ppocrv5/rec/rec.onnx',
    cls_model_dir='./models/ppocrv5/cls/cls.onnx',
    use_angle_cls=True,
    use_gpu=False  # 设置为 True 启用 GPU 加速
)

# 加载图像
img = cv2.imread('images/jinitaimei.png')

# 执行 OCR 识别
result = ocr.ocr(img, cls=True)

# 打印识别结果
for box in result[0]:
    print(f"文本: {box[1][0]}, 置信度: {box[1][1]:.4f}, 坐标: {box[0]}")
```

## 运行示例
项目提供了多个使用示例：

```bash
# 单张图像 OCR 识别
python one_sample_ocr.py

# 批量图像 OCR 识别
python batch_ocr.py

# 测试 OCR-Tiny 功能
python test_ocr_tiny.py
```

## 模型说明
项目使用 PaddleOCR v5 模型，包含三个主要部分：
- **检测模型 (det)**：负责定位图像中的文本区域
- **分类模型 (cls)**：负责判断文本的方向，提高识别准确率
- **识别模型 (rec)**：负责识别文本内容

模型以 ONNX 格式提供，位于 `models/ppocrv5/` 目录下。

## 注意事项
1. 确保模型文件路径正确
2. 使用 GPU 加速时，请安装支持 GPU 的 onnxruntime 版本
3. 对于复杂场景的图像，可能需要调整参数以获得最佳识别效果
4. 模型对清晰度高、文本区域明显的图像识别效果最佳

## 致谢
本项目基于 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 和 [OnnxOCR](https://github.com/jingsongliujing/OnnxOCR.git) 开发，感谢相关团队提供的优秀模型和技术支持。