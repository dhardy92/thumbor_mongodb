#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/dhardy92/thumbor

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 figarocms dhardy@figarocms.fr

import base64
from pymongo import Connection
from bson.objectid import ObjectId

def __conn__(context):
        connection = Connection(context.config.MONGO_LOADER_CNX_STRING)
        db = connection[context.config.MONGO_LOADER_SERVER_DB]
        storage = db[context.config.MONGO_LOADER_SERVER_COLLECTION]

        return connection, db, storage

def load(context, url, callback):
    connection, db, storage = __conn__(context)
    try:
        document = storage.find_one({ '_id': ObjectId(url) }, { context.config.MONGO_LOADER_DOC_FIELD: True })
        file_data = base64.b64decode(document[context.config.MONGO_LOADER_DOC_FIELD])
        callback(file_data)
    except (KeyError, TypeError):
        callback(None)
