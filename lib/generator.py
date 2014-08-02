#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import bard
from random import randint
import sqlite3
import os
import shutil


# rows are : Patent, Title, Abstract
conn_patents = sqlite3.connect('./data/Patents.sqlite3')
patents = conn_patents.cursor()

# some characters to avoid
stopwords=["(", ")", "/"]

class ObjectGenerator(object):
    '''
    Generate description

    '''

    def __init__(self, _corpusdir, _objects_properties, *args, **kwargs):

        self.corpusdir = _corpusdir
        self.properties=_objects_properties
        self.corpus=[]

        # remove old dir if it already exists
        if os.path.isdir(self.corpusdir):
            shutil.rmtree(self.corpusdir)
    
    def get_column_names(self,_table):
        cols= _table.execute("PRAGMA table_info('Patents');")
        for c in cols: print c

    def add_patent_data_to_corpus(self,_count, random=False):
        # self.get_column_names(patents)
        max_id = [max[0] for max in patents.execute("SELECT MAX(Id) FROM Patents;")][0]

        order=" ORDER BY id ASC "

        if (random==True) :
            ids=""
            rands=[ randint(1,max_id) for x in range(0,_count)]
            for i,id in enumerate(rands):
                ids+=""+str(id)+""
                if i != _count-1: ids+="," 
            # print ids

            order = " AND id IN ("+ids+")"

        query="SELECT * FROM Patents WHERE (Description!='')" + order + " LIMIT "+ str(_count)
        # print query

        for row in patents.execute(query):
            # print row[2]
            # remove numbers and some unwantable characters
            text=''.join([i for i in row[2] if not i.isdigit() and i not in stopwords])
            self.corpus.append(text)

    def generate_corpus_files(self):

        # Make new dir for the corpus.
        if not os.path.isdir(self.corpusdir):
            os.mkdir(self.corpusdir)

        # Output the files into the directory.
        filename = 0
        for text in self.corpus:
            filename+=1
            with open(os.path.join(self.corpusdir,str(filename)+'.txt'),'w') as fout:
                print>>fout, text
                return

    def load_corpus(self):
        
        if len(self.corpus) == 0:
            raise Exception('No corpus defined.')

        if os.path.isdir(self.corpusdir) is False:
            self.generate_corpus_files()

        newcorpus = PlaintextCorpusReader(self.corpusdir, '.*')

        bard.sents = newcorpus.sents
        bard.tokens = newcorpus.words()

        print 'init markov NLG text generator'
        self.generator = bard.generators.markov.IntelligentMarkovGenerator(bard.tokens)

    def generate_definition(self, _nb_sentences,_word_count):

        try:
            self.generator
        except Exception, e:
            self.load_corpus()

        defs=[]
        for e in range(0,_nb_sentences):
            s=self.generator.generate(length=_word_count) 
            definition=""
            for e in s: definition+=str(e)+" " # definition to str
            # print definition
            defs.append(definition)
        return defs

