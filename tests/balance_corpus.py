#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import unittest
import os

from _helpers import TestHelpers
helpers = TestHelpers()
helpers.add_relative_path()

from lib.generator import ObjectGenerator

A = 80
B = 20
total_length = 15000

if A + B != 100:
    raise ValueError("Error : total percent should be 100%")

book_dir = "../_data/books"
if not os.path.isdir(book_dir):
    raise ValueError("Error : directory doesn't exist")

bookA = os.path.join(book_dir, "science.txt")
bookB = os.path.join(book_dir, "hamlet.txt")

textA = open(bookA, 'r').read()
textB = open(bookB, 'r').read()

# print len(textA)
# print len(textB)
corpus = ""
corpus += textA[0: 15000 * A / 100]
corpus += textB[0: 15000 * B / 100]

if len(corpus) != total_length:
    raise ValueError(
        "Error : bad corpus length: %d should be %d" % (len(corpus), total_length))


# ObjectGenerator()
test_corpus_path = os.path.join(os.getcwd(), 'test_corpus')
weird_object = ObjectGenerator(test_corpus_path)

weird_object.add_to_corpus(corpus)

# create corpus
weird_object.load_corpus()

# print "weird_object",len(weird_object.corpus)
descriptions = weird_object.generate_definition(3, 15)

print descriptions
