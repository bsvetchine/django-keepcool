#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(ROOT, fname)).read()

setup(
    name="tandoori-keepcool",
    version="1.0.0",
    url="",
    license="MIT",
    description="",
    long_description=read("README.md"),
    author="Bertrand Svetchine",
    author_email="bertrand.svetchine@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Django",
        "Topic :: Software Development"],
)
