#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='requestdriver',
    version='0.1.0',
    author='Shapeways',
    author_email='api@shapeways.com',
    install_requires=[
        'requests',
    ],
    tests_require=[
        'mock'
    ],
    test_suite='testing.tests',
    setup_requires=[],
    description='Python requests wrapper for making session-based requests with some useful methods',
    url='http://gitlab.nyc.shapeways.net/quality/requestdriver',
)

