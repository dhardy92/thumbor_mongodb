#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license

# HBASE STORAGE OPTIONS
from thumbor.config import Config
Config.define('MONGO_LOADER_CNX_STRING', 'localhost')
Config.define('MONGO_LOADER_SERVER_DB', 'thumbor')
Config.define('MONGO_LOADER_SERVER_COLLECTION', 'images')
Config.define('MONGO_LOADER_DOC_FIELD', 'content')

__version__ = "0.1"
