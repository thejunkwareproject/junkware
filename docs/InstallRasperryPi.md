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
    
    mongo http://192.168.1.119:28017

    # domain name
    # http://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/
    # http://www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/
    sudo apt-get install avahi-daemon

    # INSTALL JUNKWARE
    git clone http://github.com/clemsos/junkware


