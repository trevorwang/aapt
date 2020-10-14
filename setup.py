#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
File: setup.py
Project: aapt2
Description:
Created By: Tao.Hu 2019-07-08
-----
Last Modified: 2020-10-14 02:03:42 pm
Modified By: Trevor Wang
-----
'''
from setuptools import setup, find_packages
import os
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="aapt2",
    version=os.environ.get('RELEASE_VERSION') or "0.0.2",
    keywords=("aapt2", "apktool"),
    description="Android Asset Packaging Tool for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevorwang/aapt",
    author="Trevor Wang",
    author_email="trevor.wang@qq.com",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        'aapt2': ["bin/**/*"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5, <4',
    zip_safe=False
)
