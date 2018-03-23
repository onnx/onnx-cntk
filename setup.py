#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

from distutils.core import setup
from setuptools import find_packages
import os


with open(os.path.join(os.path.dirname(__file__), "dependencies.txt"), "r") as f:
    requirements = [_.strip('\n') for _ in f.readlines()]
                                
packages = find_packages()
assert packages

setup(
    name='onnx-cntk',
    version='1.0.0.0',
    description="Runs ONNX tests and models on CNTK backend",
    license='MIT License',
    author='Microsoft Corporation',
    author_email='onnx@microsoft.com',
    url='https://github.com/onnx/onnx-cntk',
    packages=packages,
    include_package_data=True,
    install_requires=requirements
)