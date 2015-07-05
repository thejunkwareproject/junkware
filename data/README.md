# Junkware Data Sets

Datasets use to NLG for the [Junkware](http://junkware.io) installation.

## Patent Data

Patent data comes from the [Fung Institute](https://github.com/funginstitute/downloads) at UC Berkeley

    mkdir data && cd data
    # wget https://s3.amazonaws.com/fungpat_olddata/patdesc.sqlite3
    wget https://s3.amazonaws.com/fungpat_olddata/patent.sqlite3
    # wget https://s3.amazonaws.com/fungpat_olddata/class.sqlite3

    # build data
    python parse_data.py

## Wikipedia Data

Wikipedia data use the [Wiki Crawl](https://github.com/guokr/wikicrawl) project to extract articles by categories. 

* It is a clojure project, so you should use ``leiningen``. 
* Change the [app.clj](https://github.com/guokr/wikicrawl/blob/master/src/wikicrawl/app.clj) according to your settings
* ``lein run`` in your terminal

## Twitter Feelings data

Extracted tweets containing "I feel" or "I am feeling" following [We Feel Fine](http://wefeelfine.org/methodology.html) recommandations. Tweets are collecting from Twitter using Martin Hawskey's [TAGS V 5.1](http://sblasi2.blogspot.be/2013/02/instructions-for-tags-v50.html) spreadsheet app. 

[Download the data](http://docs.google.com/feeds/download/spreadsheets/Export?key=0ArNEXxu0b66PdHhBLTVjczVwMHBqQTBtdE1Tc0o0b1E&exportFormat=csv&gid=0)

Download feeling list from We Feel Fine

    cd feelings && wget http://wefeelfine.org/data/files/feelings.txt
