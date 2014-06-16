#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="requestdriver",
    version='0.0.1',
    author='Justin Iso',
    author_email="justin@shapeways.com",
    packages=find_packages(),
    install_requires=[
        'requests==2.2.1',
    ],
    setup_requires=[],
    description="Python requests wrapper for making session-based requests with some useful methods",
    url='http://gitlab.nyc.shapeways.net/quality/requestdriver',
)

