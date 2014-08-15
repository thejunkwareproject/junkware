#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lib.generator import ObjectGenerator
from lib.nlp import NLP
from lib.corpus import *

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Create an object
test_corpus_path = os.path.join(os.getcwd(), 'data/test')
weird_presentation = ObjectGenerator(test_corpus_path, keep=True)

# create corpus
weird_presentation.load_corpus()

# print "weird_object",len(weird_object.corpus)
presentation = weird_presentation.generate_definition(1, 15)
print presentation

# Create an object
test_corpus_path = os.path.join(os.getcwd(), 'data/test_patent')
weird_description = ObjectGenerator(test_corpus_path, keep=True)

# create corpus
weird_description.load_corpus()

# print "weird_object",len(weird_object.corpus)
description = weird_description.generate_definition(1, 15)
print description
