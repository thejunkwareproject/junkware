#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lib.generator import ObjectGenerator
from lib.nlp import NLP

# vars
test_corpus_path = os.path.join(os.getcwd(), 'data/corpus')

'./data/Patents.sqlite3'

# Generate an object
weird_object = ObjectGenerator(test_corpus_path, {})
weird_object.add_patent_data_to_corpus(10, random=True)
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
