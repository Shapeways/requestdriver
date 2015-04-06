#!/usr/bin/env python

from setuptools import setup

setup(
    name='requestdriver',
    version='0.1.1',
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
    url='https://github.com/shapeways/requestdriver',
)

