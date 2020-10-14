#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
File: /setup.py
Project: aapt2
Description:
Created By: Tao.Hu 2019-07-08
-----
Last Modified: 2020-10-14 02:03:42 pm
Modified By: Trevor Wang
-----
'''
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aapt2",
    version="0.0.2",
    keywords=("aapt2", "apktool"),
    description="Android Asset Packaging Tool for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevorwang/aapt",
    author="Trevor Wang",
    author_email="trevor.wang@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.3',
)
