#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name='rr-control',
    packages=find_packages(),
    version='1.0',
    description='Roony tool for control',
    author='robot-ronny',
    author_email='karel.blavka@hardwario.com',
    url='https://github.com/robot-ronny/rr-control',
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords=['robot', 'ronny', 'mqtt'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Environment :: Console'
    ],
    entry_points={
        'console_scripts': [
            'rr-control-wheels = rr_control.wheels:main',
            'rr-control-body = rr_control.body:main',
            'rr-control-eye = rr_control.eye:main',

        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
