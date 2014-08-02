#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestHelpers:
    def __init__(self):
        print "loading test helpers..."

    def add_relative_path(self):
        from os import sys, path
        root_path=path.dirname(path.dirname(path.abspath(__file__)))
        print "'" + root_path+"' added to path"
        sys.path.append(root_path)
        # sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

