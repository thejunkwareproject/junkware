#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import bard
import os
import shutil
import codecs
from lib.nlp import NLP
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class ObjectGenerator(object):

    '''
    Generate description

    '''

    def __init__(self, _corpusdir, keep=False, *args, **kwargs):

        self.corpusdir = _corpusdir
        self.corpus = []

        if keep is False:
            # remove old dir if it already exists
            if os.path.isdir(self.corpusdir):
                shutil.rmtree(self.corpusdir)

    def add_to_corpus(self, text):
        if(type(text) is not str):
            raise TypeError("Corpus should be a text.")
        txt = NLP(text)
        clean = txt.get_clean_text()
        # print clean
        self.corpus.append(clean)

    def generate_corpus_files(self):

        print "len(self.corpus)", len(self.corpus)

        # Make new dir for the corpus.
        if not os.path.isdir(self.corpusdir):
            os.mkdir(self.corpusdir)

        # Output the files into the directory.
        filename = 0
        for text in self.corpus:
            filename += 1
            with codecs.open(os.path.join(self.corpusdir, str(filename) + '.txt'), 'w', 'utf-8') as fout:
                print>>fout, text
        return

    def load_corpus(self):

        if len(self.corpus) == 0:
            raise Exception('No corpus defined.')

        if os.path.isdir(self.corpusdir) is False:
            self.generate_corpus_files()

        newcorpus = PlaintextCorpusReader(self.corpusdir, '.*')

        # bard.sents = newcorpus.sents
        bard.tokens = newcorpus.words()
        print len(bard.tokens)

        # print 'init markov NLG text generator'
        self.generator = bard.generators.markov.IntelligentMarkovGenerator(bard.tokens)

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

        return " ".join([d for d in defs])


import random

class MarkovGenerator(object):

    def __init__(self, _txt):
        self.cache = {}
        self.words = _txt.split()
        self.word_size = len(self.words)
        self.database()

    def triples(self):
        """ Generates triples from the given data string. So if our string were
                "What a lovely day", we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_text(self, size=25):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)
