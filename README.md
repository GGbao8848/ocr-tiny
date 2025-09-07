# OCR-Tiny

OCR-Tiny 是一个轻量级的光学字符识别（OCR）工具包，基于 ONNX 运行时和 PaddleOCR 模型，提供高效、准确的文本检测和识别能力。

## 项目特点
- 轻量级：依赖库少，安装简单
- 高性能：基于 ONNX 运行时，支持 CPU 和 GPU 推理
- 准确性：使用 PaddleOCR v5 模型，提供高质量的文本检测和识别
- 易用性：API 设计简洁明了，便于集成到其他项目

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基本用法

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

## 项目结构

```
oocr-tiny/
├── example.py          # 使用示例脚本
├── images/             # 示例图像文件夹
│   └── jinitaimei.png  # 示例图像
├── models/             # 模型文件目录
│   └── ppocrv5/        # PaddleOCR v5 模型
│       ├── cls/        # 方向分类模型
│       ├── det/        # 文本检测模型
│       ├── rec/        # 文本识别模型
│       └── ppocrv5_dict.txt # 字典文件
├── ocr_tiny/           # 核心代码包
│   ├── __init__.py     # 包初始化文件
│   ├── onnx_paddleocr.py # ONNX 模型封装类
│   ├── predict_system.py # 文本检测和识别系统
│   ├── predict_det.py  # 文本检测模块
│   ├── predict_rec.py  # 文本识别模块
│   ├── predict_cls.py  # 方向分类模块
│   ├── utils.py        # 工具函数
│   └── fonts/          # 字体文件
├── requirements.txt    # 依赖列表
└── setup.py            # 安装配置文件
```

## 核心功能

### 文本检测与识别流程

OCR-Tiny 的核心功能由 `predict_system.py` 和 `onnx_paddleocr.py` 实现，主要包括以下步骤：

1. **文本检测**：使用 DB (Differentiable Binarization) 算法检测图像中的文本区域
2. **方向分类**：可选步骤，检测文本的方向，提高识别准确率
3. **文本识别**：识别检测到的文本区域中的文字内容

### 主要类和方法

- **ONNXPaddleOcr**：主要接口类，封装了整个 OCR 流程
  - `__init__(**kwargs)`：初始化 OCR 模型，可以指定各种参数
  - `ocr(img, det=True, rec=True, cls=True)`：执行 OCR 识别，返回识别结果

## 依赖项

项目依赖以下库：
- onnxruntime>=1.14.0：ONNX 模型运行时
- opencv-python>=4.7.0：图像处理
- numpy>=1.24.0：数值计算

详见 `requirements.txt`

## 使用示例

项目提供了一个完整的使用示例，可以直接运行：

```bash
python example.py
```

此示例将加载 `images/jinitaimei.png` 图像并执行 OCR 识别，然后打印详细的识别结果。

## 模型说明

项目使用的是 PaddleOCR v5 模型，包含三个主要部分：
- **检测模型 (det)**：负责定位图像中的文本区域
- **分类模型 (cls)**：负责判断文本的方向，提高识别准确率
- **识别模型 (rec)**：负责识别文本内容

这些模型以 ONNX 格式提供，位于 `models/ppocrv5/` 目录下。

## 参数说明

初始化 ONNXPaddleOcr 时，可以设置以下主要参数：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| det_model_dir | str | - | 文本检测模型路径 |
| rec_model_dir | str | - | 文本识别模型路径 |
| cls_model_dir | str | - | 方向分类模型路径 |
| use_angle_cls | bool | False | 是否使用方向分类 |
| use_gpu | bool | False | 是否使用 GPU 加速 |
| drop_score | float | 0.5 | 识别结果置信度阈值 |
| det_limit_side_len | float | 960 | 检测模型输入图像的长边限制，用于处理较大图像 |
| det_limit_type | str | "max" | 检测模型输入图像的限制类型，"max"表示限制长边的最大值 |
| det_db_thresh | float | 0.3 | DB检测算法的阈值 |
| det_db_box_thresh | float | 0.6 | DB检测算法的框阈值 |
| det_db_unclip_ratio | float | 1.5 | DB检测算法的unclip比率，影响检测框的大小 |
| det_box_type | str | "quad" | 检测框的类型，"quad"表示四边形 |

## 注意事项

1. 确保模型文件路径正确
2. 如果使用 GPU 加速，请确保安装了支持 GPU 的 onnxruntime 版本
3. 对于复杂场景的图像，可能需要调整参数以获得最佳识别效果
4. 模型对于清晰度高、文本区域明显的图像识别效果最佳

## 许可证

[请根据项目实际情况添加许可证信息]

## 致谢

本项目基于 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 开发，感谢 PaddlePaddle 团队提供的优秀模型。