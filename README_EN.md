# OCR-Tiny

OCR-Tiny is a lightweight Optical Character Recognition (OCR) toolkit based on ONNX Runtime and PaddleOCR models, providing efficient and accurate text detection and recognition capabilities.

## Project Features
- **Lightweight**: Minimal dependencies, easy installation
- **High Performance**: Based on ONNX Runtime, supports CPU and GPU inference
- **Accuracy**: Uses PaddleOCR v5 models for high-quality text detection and recognition
- **User-friendly**: Clean and intuitive API design, easy to integrate into other projects

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Basic Usage

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

## Project Structure

```
oocr-tiny/
├── example.py          # Example usage script
├── images/             # Example images folder
│   └── jinitaimei.png  # Example image
├── models/             # Model files directory
│   └── ppocrv5/        # PaddleOCR v5 models
│       ├── cls/        # Direction classification model
│       ├── det/        # Text detection model
│       ├── rec/        # Text recognition model
│       └── ppocrv5_dict.txt # Dictionary file
├── ocr_tiny/           # Core code package
│   ├── __init__.py     # Package initialization file
│   ├── onnx_paddleocr.py # ONNX model wrapper class
│   ├── predict_system.py # Text detection and recognition system
│   ├── predict_det.py  # Text detection module
│   ├── predict_rec.py  # Text recognition module
│   ├── predict_cls.py  # Direction classification module
│   ├── utils.py        # Utility functions
│   └── fonts/          # Font files
├── requirements.txt    # Dependencies list
└── setup.py            # Installation configuration file
```

## Core Features

### Text Detection and Recognition Process

The core functionality of OCR-Tiny is implemented in `predict_system.py` and `onnx_paddleocr.py`, mainly including the following steps:

1. **Text Detection**: Using DB (Differentiable Binarization) algorithm to detect text regions in images
2. **Direction Classification**: Optional step, detecting the direction of text to improve recognition accuracy
3. **Text Recognition**: Recognizing the text content in detected text regions

### Main Classes and Methods

- **ONNXPaddleOcr**: Main interface class, encapsulates the entire OCR process
  - `__init__(**kwargs)`: Initializes the OCR model, various parameters can be specified
  - `ocr(img, det=True, rec=True, cls=True)`: Performs OCR recognition, returns recognition results

## Dependencies

The project depends on the following libraries:
- onnxruntime>=1.14.0: ONNX model runtime
- opencv-python>=4.7.0: Image processing
- numpy>=1.24.0: Numerical computation

See `requirements.txt` for details

## Usage Examples

The project provides a complete usage example that can be run directly:

```bash
python example.py
```

This example will load the `images/jinitaimei.png` image and perform OCR recognition, then print detailed recognition results.

## Model Description

The project uses PaddleOCR v5 models, which include three main parts:
- **Detection Model (det)**: Responsible for locating text regions in images
- **Classification Model (cls)**: Responsible for determining the direction of text to improve recognition accuracy
- **Recognition Model (rec)**: Responsible for recognizing text content

These models are provided in ONNX format and located in the `models/ppocrv5/` directory.

## Parameter Description

When initializing ONNXPaddleOcr, the following main parameters can be set:

| Parameter Name | Type | Default Value | Description |
|----------------|------|---------------|-------------|
| det_model_dir | str | - | Path to the text detection model |
| rec_model_dir | str | - | Path to the text recognition model |
| cls_model_dir | str | - | Path to the direction classification model |
| use_angle_cls | bool | False | Whether to use direction classification |
| use_gpu | bool | False | Whether to use GPU acceleration |
| drop_score | float | 0.5 | Confidence threshold for recognition results |
| det_limit_side_len | float | 960 | Long side limit for input image of detection model, used for processing larger images |
| det_limit_type | str | "max" | Limit type for input image of detection model, "max" means limiting the maximum value of the long side |
| det_db_thresh | float | 0.3 | Threshold for DB detection algorithm |
| det_db_box_thresh | float | 0.6 | Box threshold for DB detection algorithm |
| det_db_unclip_ratio | float | 1.5 | Unclip ratio for DB detection algorithm, affecting the size of detection boxes |
| det_box_type | str | "quad" | Type of detection box, "quad" means quadrilateral |

## Notes

1. Ensure the model file paths are correct
2. If using GPU acceleration, make sure you have installed the GPU-supported version of onnxruntime
3. For images with complex scenes, parameters may need to be adjusted to obtain the best recognition results
4. The model works best for images with high clarity and obvious text regions

## License

[Please add license information according to the actual situation of the project]

## Acknowledgements

This project is developed based on [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) and [OnnxOCR](https://github.com/jingsongliujing/OnnxOCR.git). We would like to thank the relevant teams for providing excellent models and technical support.