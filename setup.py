#!/usr/bin/env python
from distutils.core import setup

setup(
    name='provisor',
    version='0.2',
    packages=['provisor'],
    scripts=[ 
        'bin/provisor-server',
        'bin/provisor-create',
        'bin/provisor-config'
    ],
    data_files=[('/etc',['provisor.conf'])],
    author='Hashbang Team',
    author_email='team@hashbang.sh',
    license='GPL 3.0',
    description='Server that provisions new users on a Linux system',
    long_description=open('README.md').read(),
    install_requires=[
        'flask',
        'python-ldap'
    ]
)
