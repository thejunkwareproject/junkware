
    WORK IN PROGRESS
    Not ready to use Yet
    
# Junkware

### App Requirements

    * [redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)
    * mongodb
    * python2.7
    * virtual env
    * openSCAD (required to export clean STL for 3D printing)
    * chromium / google-chrome

Start

    virtualenv venv
    . venv/bin/activate

Then you need to install the dependencies:

    (venv) $ pip install -r requirements.txt
    (venv) $ pip install git+git://github.com/zacharydenton/bard#egg=bard

Now it's time to download the datasets

Data Sets are available on the [junkware-data](https://github.com/clemsos/junkware-data) rep

    cd [this-git-rep]
    git clone http://github.com/clemsos/junkware-data
    
    # molecules  data
    cd molecules
    chmod +x molecules/dl_molecules.sh
    ./dl_molecules.sh # download molecules datasets


You should be able to run the application:

    (venv) $ python app.py


## Mindwave Mobile setup

The brain waves are acquired using the [Mindwave Mobile](http://store.neurosky.com/products/mindwave-mobile) device. Here are some [useful info](https://www.linkedin.com/groups/Using-MindWave-Mobile-on-linux-3572341.S.161360515) to setup on Debian.

    apt-get install bluez blueman

* pair the headset with blueman (using passcode 0000) 
* connect it to a serial port (optional)
    sudo rfcomm bind /dev/rfcomm1 20:68:9D:B8:CB:AB
* code from https://github.com/akloster/python-mindwave-mobile
* change ID 20:68:9D:B8:CB:AB

Test the data acquisition:

    (venv) $ cd tests && python read_mindwave_mobile.py


## Oxymeter CMS-50E

To get hearthbeat and other metrics, we user an oxymeter ref. CMS-50E.

Test the data acquisition

    (venv) $ cd tests/oxymon && python test_oxymon.py


## Patent-based Generator

A NLG patent-based object generator created for an art project.

    pip install -m requirements.txt     # install
    python -m textblob.download_corpora # download NLP

    # nltk.download('maxent_treebank_pos_tagger')
    # nltk.download('stopwords')
    # nltk.download('wordnet')


## Tests
You will need nosetest

    chmod +x run_tests.sh
    ./run_tests.sh          # run all tests
    ./run_tests.sh xxx.py   # run a single test
