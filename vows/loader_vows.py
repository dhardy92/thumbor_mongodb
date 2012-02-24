#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from os.path import abspath, join, dirname

from pymongo import Connection
from bson.objectid import ObjectId
from pyvows import Vows, expect
import base64

import thumbor_mongodb.loader as loader
from thumbor.context import Context
from thumbor.config import Config
from fixtures.loader_options import IMAGE_URL, IMAGE_BYTES

class MongoDBContext(Vows.Context):
    def setup(self):
        self.fixtures_folder = join(abspath(dirname(__file__)), 'fixtures')

        self.connection = Connection('localhost', 7777)
        self.collection = self.connection['thumbor']['images']
        self.collection.save({'_id': ObjectId(IMAGE_URL) , "content": base64.b64encode(IMAGE_BYTES)})

    def teardown(self):
        self.connection.drop_database('thumbor')

@Vows.batch
class MongoLoaderVows(MongoDBContext):
    class CanGetImage(Vows.Context):
        @Vows.async_topic
        def topic(self, callback):
            return loader.load(Context(config=Config(MONGO_LOADER_CNX_STRING='127.0.0.1:7777')), IMAGE_URL, callback)

        def should_not_be_null(self, topic):
            expect(topic[0]).not_to_be_null()
            expect(topic[0]).not_to_be_an_error()

        def should_have_proper_bytes(self, topic):
            expect(topic[0]).to_equal(IMAGE_BYTES)

    class GettingReturnsNoneWhenImageDoesNotExist(Vows.Context):
        @Vows.async_topic
        def topic(self, callback):
            return loader.load(Context(config=Config(MONGO_LOADER_CNX_STRING='127.0.0.1:7777')), IMAGE_URL[:-2] + '99', callback )

        def should_be_null(self, topic):
            expect(topic[0]).to_be_null()
