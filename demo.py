#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lib.generator import ObjectGenerator
from lib.nlp import NLP
from lib.corpus import *


# init patents db
patents=PatentCorpus('./data/patents/Patents.sqlite3')

# Generate Wikipedia category graph
wiki_en=WikiCorpus('./data/wikipedia',"en")
wiki_en.create_wiki_graph()


# Create an object
test_corpus_path = os.path.join(os.getcwd(), 'data/corpus')
weird_object = ObjectGenerator(test_corpus_path, {})

# add 5 random records from patents db
for patent in patents.get_records(5, random=True):
    weird_object.add_to_corpus(patent)

# add a few random articles from wikipedia
for article in wiki_en.get_random_texts():
    weird_object.add_to_corpus(article)
print wiki_en.selected

# create corpus
weird_object.load_corpus()
descriptions = weird_object.generate_definition(1, 20)

print descriptions[0]

# NLP
desc_tools = NLP(descriptions[0])

sentiment = desc_tools.analyze_sentiment()
print sentiment

print desc_tools.keywords()

print desc_tools.get_verbs()

print desc_tools.translate_to('zh')

print desc_tools.translate_to('fr')
