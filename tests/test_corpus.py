import unittest
import os
from _helpers import TestHelpers
helpers = TestHelpers()
helpers.add_relative_path()

from lib.corpus import *

wiki_corpus_path = test_corpus_path = os.path.join(
    os.getcwd(), 'data/wikipedia')

patent_db = test_corpus_path = os.path.join(
    os.getcwd(), 'data/patents/Patents.sqlite3')

'''
class WikiCorpusTestCase(unittest.TestCase):

    def setUp(self):
        self.wiki = WikiCorpus(wiki_corpus_path, "en")
        self.wiki.create_wiki_graph()

    def test_select_random_nodes(self):
        nodes = self.wiki.select_random_nodes()
        print nodes
        self.assertTrue(len(nodes) == 2)

    def test_get_corpus_from_node(self):
        nodes = self.wiki.select_random_nodes()
        files = []
        for node in nodes:
            print node
            files.append(self.wiki.get_corpus_from_node(node))
        self.assertTrue(len(files) == 2)
'''

class PatentCorpusTestCase(unittest.TestCase):

    def setUp(self):
        self.patents = PatentCorpus(patent_db)

    def test_get_column_names(self):
        cols=self.patents.get_column_names()
        self.assertTrue(len(cols) == 4, msg="message")
        self.assertTrue(cols[0] == "Id", msg="message")

    def test_get_records(self):
        pats=self.patents.get_records(2, random=True)
        self.assertTrue(len(pats) == 2)


if __name__ == '__main__':
    unittest.main()
