# test_mongo.py
'''
Test write / read on mongoDB
'''
import datetime
import unittest

from _helpers import TestHelpers
helpers=TestHelpers()
helpers.add_relative_path()

from models.junk import Junk

class ModelsTest(unittest.TestCase):

    def setUp(self):
        self.data = [
            {
             "description": "some random tests",
             "name": "My first junk",
             "tags": ["junk", "stuff", "scifi"],
             "date": datetime.datetime.utcnow()
             }
         ]

    def test_save(self):
        junk = Junk(self.data).save()
        print junk
        foo = Junk.collection.find_one({"name": self.data.name})
        print foo
        self.asserTrue(False)

    # def test_update(self):
        
    #     junk.foo

