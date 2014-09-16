#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minimongo import Model, Index, configure
import json

# mongo db
configure(host="localhost", port=27017)

db_name="junkware"

class Junk(Model):

    class Meta:
        
        # Here, we specify the database and collection names.
        # A connection to your DB is automatically created.
        database = db_name
        collection = "junks"

        # Now, we programatically declare what indices we want.
        # The arguments to the Index constructor are identical to
        # the args to pymongo"s ensure_index function.

        indices = (
            # Index("mid"),
        )

    def __init__(self, _data):
        self.
        self.


    def get_geo_entities(self):
        return self.tags.get("GPE")

    def get_loc_entities(self):
        return self.tags.get("LOC")

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
