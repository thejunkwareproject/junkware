#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
from text.blob import TextBlob as tb
 
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)
 
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)
 
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
 
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

document1=tb("hah ho ho")
document2=tb("hah ho ho")
document3=tb("hah ho ho")

 
bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))