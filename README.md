# Junkware

A NLG patent-based object generator created for an art project.


## Install

    pip install -m requirements.txt     # install
    python -m textblob.download_corpora # download NLP

    # nltk.download('maxent_treebank_pos_tagger')
    # nltk.download('stopwords')
    # nltk.download('wordnet')

## Data

Patent data comes from the [Fung Institute](https://github.com/funginstitute/downloads) at UC Berkeley

    mkdir data && cd data
    # wget https://s3.amazonaws.com/fungpat_olddata/patdesc.sqlite3
    wget https://s3.amazonaws.com/fungpat_olddata/patent.sqlite3
    # wget https://s3.amazonaws.com/fungpat_olddata/class.sqlite3

    # build data
    python parse_data.py


## Tests
You will need nosetest

    chmod +x run_tests.sh
    ./run_tests.sh          # run all tests
    ./run_tests.sh xxx.py   # run a single test
