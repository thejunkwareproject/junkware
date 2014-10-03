
    WORK IN PROGRESS
    Not ready to use Yet
    
# Junkware

Requirements

    * [redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)
    * mongodb
    * python3
    * openSCAD (required to export clean STL for 3D printing)


Start

    virtualenv venv
    . venv/bin/activate

Then you need to install the dependencies:

    (venv) $ pip install -r requirements.txt
    (venv) $ pip install git+git://github.com/zacharydenton/bard#egg=bard

Run the data acquisition:

    (venv) $ python read_mindwave_mobile.py

Run the application:

    (venv) $ python app.py

## Mindwave Mobile setup

[Useful info](https://www.linkedin.com/groups/Using-MindWave-Mobile-on-linux-3572341.S.161360515)

    apt-get install bluez blueman

* pair the headset with blueman (using passcode 0000) 
* connect it to a serial port (optional)
    sudo rfcomm bind /dev/rfcomm1 20:68:9D:B8:CB:AB
* code from https://github.com/akloster/python-mindwave-mobile
* change ID 20:68:9D:B8:CB:AB

## Patent-based Generator

A NLG patent-based object generator created for an art project.

    pip install -m requirements.txt     # install
    python -m textblob.download_corpora # download NLP

    # nltk.download('maxent_treebank_pos_tagger')
    # nltk.download('stopwords')
    # nltk.download('wordnet')

### Data

Data Sets are available on the [junkware-data](https://github.com/clemsos/junkware-data) rrep

## Tests
You will need nosetest

    chmod +x run_tests.sh
    ./run_tests.sh          # run all tests
    ./run_tests.sh xxx.py   # run a single test
