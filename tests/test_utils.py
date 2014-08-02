#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from _helpers import TestHelpers
helpers=TestHelpers()
helpers.add_relative_path()

from lib.utils import slugify

class EncodingTest(unittest.TestCase):

    def setUp(self):
        print "Testing Encoding"
        self.w=u"什么"
        self.title="blaldqsdjq d54 #{~[|ç±Êø~#{ù*ùds$'€€ haha   ajskq    "

    def test_slugify(self):
        s=slugify(self.title)
        self.assertTrue(s == "blaldqsdjq_d54_ceuuds_haha_ajskq")

if __name__ == '__main__':
    unittest.main()