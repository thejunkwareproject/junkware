import os, time, datetime
import json
from threading import Thread
import random

from gevent import monkey
monkey.patch_all()

from flask import request, abort, render_template, session, url_for
from flask.ext import restful
from flask.ext.restful import reqparse

from flask import make_response

from resources import app, api, mongo
from bson.objectid import ObjectId
from lib.queue import RedisQueue

from lib.corpus import *
from lib.generator import MarkovGenerator

# init patents db
patents=PatentCorpus('../../junkware-data/patents/Patents.sqlite3')

# socketio = SocketIO(app)
thread = None

# data queue
q = RedisQueue('mindwave')

class Junk(restful.Resource):

    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()

    def get(self, junk_id):
        return mongo.db.junks.find_one_or_404({"_id": junk_id})

    def put(self, junk_id):
        for f in request.form:
            data=json.loads(f)
        # print data
        mongo.db.junks.update({"_id": junk_id}, data)
        return mongo.db.junks.find_one({"_id": junk_id})

    def delete(self, junk_id):
        mongo.db.junks.find_one_or_404({"_id": junk_id})
        mongo.db.junks.remove({"_id": junk_id})
        return '', 204

class JunkList(restful.Resource):

    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('dna', type=str)
        super(JunkList, self).__init__()

    def get(self):
        return  [x for x in mongo.db.junks.find()]

    def post(self):
        args = self.parser.parse_args()
        print args

        # add DNA
        if not args['dna']:
            abort(400)

        # add molecule
        files=os.listdir("../../junkware-data/molecules")
        molecules=[mol for mol in files if mol[-4:][:3]=="pdb"]
        molecule = random.choice(molecules)
        print molecule
        args["molecule"]=molecule

        # add patents corpus
        pats = patents.get_records(10, random=True)
        pats_ids=pats[0]
        args["patents_ids"]=pats_ids

        # create a title
        titles=""
        for t in pats[2]:
            titles += " "+t

        args['title']= "Future Object"# MarkovGenerator(titles).generate_text(size=random.randint(4,7)).title()

        # create element for geometry
        shape={}
        shape["m1"]  = random.randint(0,20)
        shape["n11"] = random.randint(0,50)
        shape["n12"] = random.randint(0,50)
        shape["n13"] = random.randint(0,50)
        shape["m2"]  = random.randint(0,20)
        shape["n21"] = random.randint(0,50)
        shape["n22"] = random.randint(0,50)
        shape["n23"] = random.randint(0,50)

        args['shape'] = shape

        args["created_at"]=datetime.datetime.utcnow()

        junk_id =  mongo.db.junks.insert(args)
        return mongo.db.junks.find_one({"_id": junk_id})
