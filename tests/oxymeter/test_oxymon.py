#!/usr/bin/env python
#
# Copyright (C) 2011-2013 Vincent Ollivier <contact@vincentollivier.com>
#
# This file is part of Oximon.
#
# Oximon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# from argparse import ArgumentParser
from datetime import datetime
from os import path
from oximon.cms50 import CMS50
# from serial.serialutil import SerialException

if __name__ == '__main__':

    port = '/dev/ttyUSB0'
    if not path.exists(port):
        exit("oximon: could not open '%s': no such file or directory" % port)

    oximeter = CMS50(port) 

    print('#date\theart rate\toxygen saturation')
    is_finished = False
    try:
        while not is_finished:
            try:
                if oximeter.update():
                    output = [datetime.now(), oximeter.hr, oximeter.sat]
                    print('\t'.join(str(o) for o in output))
            except SerialException as e: 
                exit('oximon: %s' % e)
    except (KeyboardInterrupt, SystemExit):
        is_finished = True
    finally:
        oximeter.close()
