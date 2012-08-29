#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='drawsomething',
    version='0.1.0',
    description='Drawsomething word guess helper.',
    author='Lx Yu',
    author_email='lixinfish@gmail.com',
    packages=['drawsomething', ],
    package_data={'': ['LICENSE'], },
    scripts=['bin/drawsth'],
    url='https://github.com/lxyu/drawsomething',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    install_requires=[
        "pyenchant",
        "google_translate",
    ],
)
