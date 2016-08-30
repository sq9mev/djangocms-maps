#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import djangocms_maps as package

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='djangocms-maps',
    version=package.__version__,
    description=package.__doc__,
    author='Peter Bittner',
    author_email='django@bittner.it',
    url='https://github.com/Organice/djangocms-maps',
    packages=[
        'djangocms_maps',
        'djangocms_maps.migrations',
    ],
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
