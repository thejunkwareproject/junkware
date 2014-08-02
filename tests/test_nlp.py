#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from _helpers import TestHelpers
helpers=TestHelpers()
helpers.add_relative_path()

from lib.nlp import NLP

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''


class NLPTest(unittest.TestCase):

    def setUp(self):
        self.nlp = NLP(text)

    def test_sentences(self):
        self.assertTrue(len(self.nlp.sentences)==2)

    def test_keywords(self):
        keywords=self.nlp.keywords()
        print len(keywords)
        self.assertTrue(len(keywords) == 24)

    def test_words(self):
        words=self.nlp.words()
        print len(words)
        self.assertTrue(len(words)==72)

    def test_count_words(self):
        c=self.nlp.count_words()
        self.assertTrue(type(c) == dict)

    def test_adjectives(self):
        adj=self.nlp.get_adjectives()
        print type(adj[0])
        self.assertTrue(len(adj) == 15)
        self.assertTrue(type(adj[0]) == str)

    def test_verbs(self):
        verbs=self.nlp.get_verbs()
        print verbs
        self.assertTrue(len(verbs) == 4)
        self.assertTrue(type(verbs[0]) == str)

    def test_nouns(self):
        nouns=self.nlp.get_nouns()
        print len(nouns)
        self.assertTrue(len(nouns) == 12)
        self.assertTrue(type(nouns[0]) == str)

    def test_noun_phrases(self):
        noun_phrases=self.nlp.get_noun_phrases()
        print len(noun_phrases)
        self.assertTrue(len(noun_phrases) == 9)
    
    def test_get_language(self):
        lg=self.nlp.get_language()
        self.assertTrue(lg == "en")

    def test_sentiment(self):
        sentiments=self.nlp.analyze_sentiment()
        self.assertTrue(len(sentiments)==2)
        for sent in sentiments: 
            self.assertIsNotNone(sent["polarity"])
            self.assertTrue(type(sent["polarity"]) == float)
            self.assertIsNotNone(sent["subjectivity"])
            self.assertTrue(type(sent["subjectivity"]) == float)

    def test_translation(self):
        zh_txt=self.nlp.translate_to('zh')
        print zh_txt
        self.assertTrue(zh_txt.detect_language() == "zh-CN")


if __name__ == '__main__':
    unittest.main()