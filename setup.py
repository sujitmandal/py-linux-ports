#!/usr/bin/env python
# Author : Sujit Mandal
__author__ = 'Sujit Mandal'
#Date : 10-01-2022
from setuptools import setup 

def readme():
    with open('README.md') as files:
        README = files.read()

    return(README)

setup(
    name = 'py-linux-ports',
    version = '0.0.2',
    description = "Check Linux System Port's Status.",
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sujitmandal/py-linux-ports',
    author = 'Sujit Mandal',
    author_email = 'mandals974@gmail.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages = ['PyLinuxPorts'],
    include_package_data = True,
)