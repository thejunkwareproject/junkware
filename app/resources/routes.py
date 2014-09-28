import os
import json
from flask import render_template, jsonify, send_from_directory
from resources import app, api, mongo
from Junk import Junk, JunkList

from lib.dna import get_random_dna

# routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/junks')
def junk_index():
    junks= [x for x in mongo.db.junks.find()]
    return render_template('index.html', junks=junks)

@app.route('/junk/new')
def junk_new():
    return render_template('junk/create.html')

@app.route('/junk/partials/<path:path>')
def partials(path):
    print path
    return render_template(os.path.join('partials',path+".html"))

@app.route('/data/dna')
def get_dna():
    my_dna=get_random_dna()
    return jsonify({"dna":my_dna})

@app.route('/data/molecules')
def get_molecules_list():
    files=os.listdir("../../junkware-data/molecules")
    molecules=[mol for mol in files if mol[-4:][:3]=="pdb"]
    print molecules
    return jsonify({"molecules":molecules})

@app.route('/data/molecules/<path:path>')
def get_molecule(path):
    app_path =os.path.dirname(os.path.abspath(os.getcwd()))
    data_path= os.path.join(os.path.dirname(app_path), 'junkware-data')
    molecule_path=os.path.join(data_path, "molecules")

    # print fp,os.path.isfile(fp)
    # with open(fp,"r") as f :
    #     print f.readlines()
    return send_from_directory(molecule_path, path)

# API
api.add_resource(JunkList, '/api/junks')
api.add_resource(Junk, '/api/junk/<ObjectId:junk_id>')

# STATIC
@app.route('/js/<path:path>')
def js_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('js', path))

@app.route('/css/<path:path>')
def css_static_proxy(path):
    print os.path.join('css', path)
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('css', path))

@app.route('/lib/<path:path>')
def lib_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('lib', path))

@app.route('/libs/<path:path>')
def libs_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('libs', path))

@app.route('/img/<path:path>')
def img_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('img', path))

@app.route('/data/<path:path>')
def data_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('data', path))
