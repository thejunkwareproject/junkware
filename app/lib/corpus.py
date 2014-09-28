# -*- coding: utf-8 -*-

import os
from fnmatch import fnmatch
import yaml
import networkx as nx
from utils import nx_to_gv_file, nx_to_gephi_csv, slugify
from random import choice, randint
import sqlite3
import codecs
import pickle

from nlp import NLP

# some characters to avoid
stopwords = ["(", ")", "/"]

class WikiCorpus(object):

    '''
    Generate Wikipedia corpus

    '''

    def __init__(self, corpusdir, language):
        self.language = language
        self.wk_path = os.path.join(corpusdir, language)
        self.out_path = os.path.join(corpusdir, "out")
        print self.wk_path
        self.selected=[]
        
        self.graph_path = os.path.join(self.wk_path,'graph.txt')
        
        if not os.path.isfile(self.graph_path):
            self.categories = nx.Graph()
            self.create_wiki_graph()
        else:
            print "load graph : %s"%self.graph_path
            self.categories = pickle.load(open(self.graph_path))

    def create_wiki_graph(self):
        """ Create wiki graph representation of categories"""

        print 'Creating wiki corpus graph representation'

        for path, subdirs, files in os.walk(self.wk_path):

            here = os.path.split(path)[1]
            parent = os.path.split(os.path.split(path)[0])[1]

            self.categories.add_edge(parent, here)

            self.categories[parent]["path"] = path
            self.categories[here]["path"] = path

            for name in files:
                if fnmatch(name, "*.yaml") and "Index" not in name and "index" not in name:  # check if there is a text file
                    
                    category_name = name[0:-5]
                    yaml_file_path = os.path.join(
                        path, category_name + ".yaml")

                    # yaml
                    yaml_file = open(yaml_file_path, "r")
                    docs = yaml.load_all(yaml_file)

                    # category_name
                    for doc in docs:
                        cat_parent = doc["CategoryPath"][0]

                        self.categories.add_edge(
                            slugify(cat_parent), slugify(category_name))
                        self.categories[slugify(cat_parent)]["path"] = path
                        self.categories[slugify(category_name)]["path"] = path

                        for cat in doc["Categories"][0][self.language]:
                            self.categories.add_edge(
                                slugify(category_name), slugify(cat))
                            self.categories[slugify(cat)]["path"] = path

        print("The categories graph %s has %d nodes with %d edges"
              % (self.categories.name,
                 nx.number_of_nodes(self.categories),
                 nx.number_of_edges(self.categories)))
        for node in nx.nodes(self.categories):
            self.get_corpus_from_node(node)

        pickle.dump(self.categories, open(self.graph_path, 'w'))

        print "Graph saved as %s"%(self.graph_path)

    def create_wiki_graphviz(self, path):
        ''' Visualize the wiki corpus with Graphviz '''
        nx_to_gv_file(self.categories, "wiki_categories", path)

    def create_wiki_gephi_files(self, path):
        ''' Generate CSV files for Gephi'''
        nx_to_gephi_csv(self.categories, "wiki_categories", path)

    def get_random_nodes(self):
        ''' Select two random nodes from the graph
            return a tuple of 2 nodes
        '''

        first_node = choice(self.categories.nodes())  # pick a random node

        possible_nodes = set(self.categories.nodes())
        neighbours = self.categories.neighbors(first_node) + [first_node]

        # remove the first node and all its neighbours from the candidates
        possible_nodes.difference_update(neighbours)
        second_node = choice(list(possible_nodes))      # pick second node

        self.selected+=[first_node, second_node]
        return [first_node, second_node]

    def get_corpus_from_node(self, node):
        '''
        Retrieve a set of text file paths from category graph node
        return a [] of texts path
        '''
        texts = []
        for myfile in os.listdir(self.categories[node]["path"]):
            if myfile.endswith(".txt"):
                path=os.path.join(self.categories[node]["path"], myfile)
                with codecs.open (path, "r", "utf-8") as myfile:
                    text=myfile.read().replace('\n', '')
                    result=NLP(text).get_clean_text()
                    texts.append(result.encode("utf-8"))
        return texts

    def get_random_texts(self):
        """ retrieve a set of texts based on 2 random categories"
        """
        texts=[]
        nodes=self.get_random_nodes()
        for node in nodes:
            texts+=self.get_corpus_from_node(node)
        return texts

class PatentCorpus(object):

    """ Patent corpus """

    def __init__(self, patent_db):
        conn_patents = sqlite3.connect(patent_db)
        self.patents = conn_patents.cursor()

    def get_column_names(self):
        ''' Rows should be : Patent, Title, Abstract '''
        cols=[]
        for c in self.patents.execute("PRAGMA table_info('Patents');"): cols.append(c[1])
        return cols

    def get_records(self, _count, random=False):

        """
            Get a number of patents
            return :
            patents in full text
        """

        abtracts=[]
        titles=[]

        max_id = [max[0] for max in self.patents.execute("SELECT MAX(Id) FROM Patents;")][0]
        order = " ORDER BY id ASC "

        if (random == True):
            ids = ""
            rands = [randint(1, max_id) for x in range(0, _count)]
            for i, _id in enumerate(rands):
                ids += "" + str(_id) + ""
                if i != _count - 1:
                    ids += ","

            order = " AND id IN (" + ids + ")"

        query = "SELECT * FROM Patents WHERE (Description!='')" + \
            order + " LIMIT " + str(_count)
        # print query

        for row in self.patents.execute(query):
            # print row[3]
            # remove numbers and some unwantable characters
            text = ''.join(
                [i for i in row[2] if not i.isdigit() and i not in stopwords])

            abtracts.append(str(text))
            titles.append(str(row[3]))

        return ids, abtracts, titles

    def get_records_by_ids(self, _ids):

        abtracts=[]
        titles=[]

        my_ids=str(_ids).split(",")

        ids = ""
        for i, _id in enumerate(my_ids):
            ids += "" + str(_id) + ""
            if i != len(my_ids) - 1:
                ids += ","

        order = " AND id IN (" + ids + ")"

        query = "SELECT * FROM Patents WHERE (Description!='')" + \
            order + " LIMIT " + str(len(my_ids))

        for row in self.patents.execute(query):
            text = ''.join(
                [i for i in row[2] if not i.isdigit() and i not in stopwords])

            abtracts.append(str(text))
            titles.append(str(row[3]))


        return abtracts, titles


