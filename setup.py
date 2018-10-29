#!/usr/bin/python
# -*- encoding: utf-8 -*-

# !/usr/bin/python
# -*- encoding: utf-8 -*-

from sqlite3 import connect

from setuptools import setup
from setuptools.command.install import install

from pycargr import DB_PATH


class CustomInstall(install):

    def run(self):
        install.run(self)

        with connect(str(DB_PATH)) as db_con:
            db_con.executescript(open('schema.sql').read())


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
    url='https://github.com/Florents-Tselai/PyCarGr',
    cmdclass={'install': CustomInstall},
    entry_points={
        'console_scripts': ['pycargr=pycargr.cli:main'],
    }

)
