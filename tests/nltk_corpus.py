# Create a new corpus by specifying the parameters
# (1) directory of the new corpus
# (2) the fileids of the corpus
# NOTE: in this case the fileids are simply the filenames.
newcorpus = PlaintextCorpusReader(corpusdir, '.*')

# Access each file in the corpus.
for infile in sorted(newcorpus.fileids()):
    print infile # The fileids of each file.
    with newcorpus.open(infile) as fin: # Opens the file.
        print fin.read().strip() # Prints the content of the file
print

# Access the plaintext; outputs pure string/basestring.
print newcorpus.raw().strip()
print 

# Access paragraphs in the corpus. (list of list of list of strings)
# NOTE: NLTK automatically calls nltk.tokenize.sent_tokenize and 
#       nltk.tokenize.word_tokenize.
#
# Each element in the outermost list is a paragraph, and
# Each paragraph contains sentence(s), and
# Each sentence contains token(s)
print newcorpus.paras()
print

# To access pargraphs of a specific fileid.
print newcorpus.paras(newcorpus.fileids()[0])

# Access sentences in the corpus. (list of list of strings)
# NOTE: That the texts are flattened into sentences that contains tokens.
print newcorpus.sents()
print

# To access sentences of a specific fileid.
print newcorpus.sents(newcorpus.fileids()[0])

# Access just tokens/words in the corpus. (list of strings)
print newcorpus.words()

# To access tokens of a specific fileid.
print newcorpus.words(newcorpus.fileids()[0])