
    WORK IN PROGRESS
    Not ready to use Yet
    
# Junkware

Requirements

    * [redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis)
    * mongodb
    * python3


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


## Install on Raspberry Pi


    # mongo at 
    nmap -p 22 --open -sV 192.168.1.0/24
    sudo  mount -t vfat -o loop,offset=4194304 /dev/mmcblk0p1 /media/usb

    pi@192.168.1.118 # eth0
    pi@192.168.1.119 # wlan0

    su - 
    
    raspi-config # setup locales
    apt-get update
    apt-get upgrade

    
    # python tools
    sudo apt-get install python-dev python-pip python-virtualenv
    
    # http://www.widriksson.com/install-mongodb-raspberrypi/

    # domain name
    # http://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/
    # http://www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/
    sudo apt-get install avahi-daemon

    # INSTALL JUNKWARE
    git clone http://github.com/clemsos/junkware


