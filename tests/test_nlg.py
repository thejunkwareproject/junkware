#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import shutil

from _helpers import TestHelpers
helpers=TestHelpers()
helpers.add_relative_path()

from lib.generator import ObjectGenerator

test_corpus_path = os.path.join(os.getcwd(),'tests/test_corpus')

test_text='''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

class ObjectGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.object = ObjectGenerator(test_corpus_path,{})
        self.object.corpus.append(test_text)
        self.object.add_patent_data_to_corpus(2, random=True)

    def test_add_patent_data_to_corpus(self):
        self.object.add_patent_data_to_corpus(2, random=True)
        self.assertTrue(len(self.object.corpus)==5)

    def test_generate_corpus(self):
        
        if os.path.isdir(test_corpus_path):
            shutil.rmtree(test_corpus_path)

        self.object.generate_corpus()
        self.assertTrue(os.path.isdir(test_corpus_path)==True)

        filename=os.path.join(test_corpus_path,"1.txt")
        self.assertTrue(os.path.isfile(filename)==True)

        text = open(filename, 'r').read()
        print test_text[0:4],text[0:4]
        self.assertTrue(test_text[0:4]==text[0:4])

    def test_load_nltk_corpus(self):
        self.object.load_nltk_corpus()
        self.assertIsNotNone(self.object.generator)

    def _generate_text(self):
        length=10
        items=1
        s=self.object.generate_definition(1,10);
        self.assertTrue(len(s)==items)
        self.assertTrue(type(s[0])==str)

if __name__ == '__main__':
    unittest.main()