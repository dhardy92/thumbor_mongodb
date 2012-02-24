#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 Damien Hardy dhardy@figarocms.fr

from distutils.core import setup
from thumbor_hbase import __version__

setup(
    name = "thumbor_mongodb",
    packages = ["thumbor_mongodb"],
    version = __version__,
    description = "MongoDB loader for Thumbor (no GridFS)",
    author = "Damien Hardy",
    author_email = "dhardy@figarocms.fr",
    keywords = ["thumbor", "mongodb", "images"],
    license = 'MIT',
    url = 'https://github.com/dhardy92/thumbor_hbase',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_mongodb": "thumbor_mongodb"},
    install_requires=["thumbor","pymongo"],
    long_description = """\
Thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
This module provide support for MongoDB loader for images. 
Image data is stored in one field of MongoDB document in a collection and addressed by its ObjectId('_id')
"""
)
