#!/usr/bin/env python3
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twister-spinner", #
    version="1.0.0",
    author="Craig Warner",
    author_email="cgwarner2014@gmail.com",
    description="Twwister Spinner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craig-warner/MandelbrotBackground",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    #install_requires=['PyQt5>=5.8.0','hjson>=3.1.0','jsonformatter>=0.3.2','argparse>=1.4.0'],
    install_requires=['hjson>=3.1.0','jsonformatter>=0.3.2','argparse>=1.4.0'],
    scripts=['bin/twister-spinner',
            "bin/version.py"
            ],
)