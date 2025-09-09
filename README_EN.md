# OCR-Tiny

OCR-Tiny is a lightweight Optical Character Recognition (OCR) toolkit based on ONNX Runtime and PaddleOCR models, providing efficient and accurate text detection and recognition capabilities.

## Project Introduction
OCR-Tiny aims to provide a simple, easy-to-use, high-performance OCR solution for various scenarios that need to extract text information from images.

## Project Advantages
- **Lightweight**: Minimal dependencies, easy installation
- **High Performance**: Based on ONNX Runtime, supports CPU and GPU inference
- **Accuracy**: Uses PaddleOCR v5 models for high-quality text detection and recognition
- **User-friendly**: Clean and intuitive API design, easy to integrate into other projects

## Environment Requirements
- Python 3.7+ environment
- Main dependencies:
  - onnxruntime>=1.14.0: ONNX model runtime
  - opencv-python>=4.7.0: Image processing
  - numpy>=1.24.0: Numerical computation

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Basic Usage
```python
import cv2
from ocr_tiny import ONNXPaddleOcr

# Initialize OCR model
ocr = ONNXPaddleOcr(
    det_model_dir='./models/ppocrv5/det/det.onnx',
    rec_model_dir='./models/ppocrv5/rec/rec.onnx',
    cls_model_dir='./models/ppocrv5/cls/cls.onnx',
    use_angle_cls=True,
    use_gpu=False  # Set to True to enable GPU acceleration
)

# Load image
img = cv2.imread('images/jinitaimei.png')

# Perform OCR recognition
result = ocr.ocr(img, cls=True)

# Print recognition results
for box in result[0]:
    print(f"Text: {box[1][0]}, Confidence: {box[1][1]:.4f}, Coordinates: {box[0]}")
```

## Run Examples
The project provides several usage examples:

```bash
# Single image OCR recognition
python one_sample_ocr.py

# Batch image OCR recognition
python batch_ocr.py

# Test OCR-Tiny functionality
python test_ocr_tiny.py
```

## Model Description
The project uses PaddleOCR v5 models, which include three main parts:
- **Detection Model (det)**: Responsible for locating text regions in images
- **Classification Model (cls)**: Responsible for determining the direction of text to improve recognition accuracy
- **Recognition Model (rec)**: Responsible for recognizing text content

These models are provided in ONNX format and located in the `models/ppocrv5/` directory.

## Notes
1. Ensure the model file paths are correct
2. When using GPU acceleration, please install the GPU-supported version of onnxruntime
3. For images with complex scenes, parameters may need to be adjusted to obtain the best recognition results
4. The model works best for images with high clarity and obvious text regions

## Acknowledgements
This project is developed based on [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) and [OnnxOCR](https://github.com/jingsongliujing/OnnxOCR.git). We would like to thank the relevant teams for providing excellent models and technical support.