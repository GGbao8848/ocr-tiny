#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ocr-tiny',
    version='0.1.0',
    description='轻量级ONNX格式OCR工具包',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    package_data={
        'ocr_tiny': ['fonts/*'],
    },
    include_package_data=True,
    install_requires=[
        'onnxruntime>=1.14.0',
        'opencv-python>=4.7.0',
        'numpy>=1.24.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)