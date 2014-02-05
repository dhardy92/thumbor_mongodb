#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license

# HBASE STORAGE OPTIONS
from thumbor.config import Config
Config.define('MONGO_LOADER_CNX_STRING', 'localhost', "MongodDB connexion string", 'mongo_loader')
Config.define('MONGO_LOADER_SERVER_DB', 'thumbor', 'MongoDB database', 'mongo_loader')
Config.define('MONGO_LOADER_SERVER_COLLECTION', 'images', 'MongoDB Collection', 'mongo_loader')
Config.define('MONGO_LOADER_DOC_FIELD', 'content', 'MongoDB document field used for image content', 'mongo_loader')

__version__ = "0.2"
