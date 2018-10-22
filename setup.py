#!/usr/bin/python
# -*- encoding: utf-8 -*-

from distutils.core import setup

setup(
    name='PyCarGr',
    version='1.0.0',
    packages=['pycargr', ],
    license='The MIT License (MIT) Copyright © 2017 Florents Tselai.',
    description='PyCarGr - Unofficial car.gr API',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    install_requires=open('requirements.txt', 'r').readlines(),
    author='Florents Tselai',
    author_email='florents.tselai@gmail.com',
    url='https://github.com/Florents-Tselai/PyCarGr'
)
