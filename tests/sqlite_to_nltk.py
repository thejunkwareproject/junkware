from lib.generator import PhraseGenerator
import sqlite3
import time
import nltk

start_time = time.clock()

# open existing database
conn = sqlite3.connect('./data/patdesc.sqlite3')
cursor = conn.cursor()

lines = 0

for row in cursor.execute("SELECT * FROM patdesc WHERE (abstract!='') LIMIT 1000" ):
    # keywords(row[1])
    # tokens = nltk.word_tokenize(row[1])
    # print tokens
    # gen = PhraseGenerator(nltk.corpus.inaugural)
    print row[1]
    
    # print gen(row[1])

names = list(map(lambda x: x[0], cursor.description))
print names


conn.close()


elapsed_time = time.clock() - start_time
print "Time elapsed: {} seconds".format(elapsed_time)
print "Read {} lines".format(lines)
