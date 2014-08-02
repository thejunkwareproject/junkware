#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import sqlite3

conn = sqlite3.connect('./data/patdesc.sqlite3')
cursor = conn.cursor()


corpus = []
corpusdir = 'tests/test_corpus/'

stopwords=["(", ")", "/"]
for row in cursor.execute("SELECT * FROM patdesc WHERE (abstract!='') LIMIT 10" ):
    text= ''.join([i for i in row[1] if not i.isdigit() and i not in stopwords])
    corpus.append(text)


# Make new dir for the corpus.
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)

# Output the files into the directory.
filename = 0
for text in corpus:
    filename+=1
    with open(corpusdir+str(filename)+'.txt','w') as fout:
        print>>fout, text

# Check that our corpus do exist and the files are correct.
# assert os.path.isdir(corpusdir)
# for infile, text in zip(sorted(os.listdir(corpusdir)),corpus):
#     assert open(corpusdir+infile,'r').read().strip() == text.strip()
