#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import bard
import os
import shutil

class ObjectGenerator(object):

    '''
    Generate description

    '''

    def __init__(self, _corpusdir, _objects_properties, *args, **kwargs):

        self.corpusdir = _corpusdir
        self.properties = _objects_properties
        self.corpus = []

        # remove old dir if it already exists
        if os.path.isdir(self.corpusdir):
            shutil.rmtree(self.corpusdir)

    def add_to_corpus(self,text):
        if(type(text) is not str):
            raise TypeError("Corpus should be a text.")
        self.corpus.append(text)

        self.corpus

    def generate_corpus_files(self):

        # Make new dir for the corpus.
        if not os.path.isdir(self.corpusdir):
            os.mkdir(self.corpusdir)

        # Output the files into the directory.
        filename = 0
        for text in self.corpus:
            filename += 1
            with open(os.path.join(self.corpusdir, str(filename) + '.txt'), 'w') as fout:
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
        self.generator = bard.generators.markov.IntelligentMarkovGenerator(
            bard.tokens)

    def generate_definition(self, _nb_sentences, _word_count):

        try:
            self.generator
        except Exception, e:
            self.load_corpus()

        defs = []
        for e in range(0, _nb_sentences):
            s = self.generator.generate(length=_word_count)
            definition = ""
            for e in s:
                definition += str(e) + " "  # definition to str
            # print definition
            defs.append(definition)
        return defs
