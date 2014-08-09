#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from _helpers import TestHelpers
helpers=TestHelpers()
helpers.add_relative_path()

# from lib.generator import ObjectGenerator
corpus_path = os.path.join(os.getcwd(),'data')

import os
from fnmatch import fnmatch


# wikipedia
pattern = "*.txt"
wk_path=os.path.join(corpus_path,'wikipedia')
for path, subdirs, files in os.walk(wk_path):
    for name in files:
        if fnmatch(name, pattern):
            print subdirs
            print os.path.join(path, name)
            print