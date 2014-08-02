#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3

# conn = sqlite3.connect('../data/class.sqlite3')
conn = sqlite3.connect('../data/Patents.sqlite3')
c = conn.cursor()

cols= c.execute("PRAGMA table_info('Patents');")
for col in cols:print col

for row in c.execute("SELECT * FROM Patents ORDER BY id DESC LIMIT 1" ):
    print row

maxid = [max[0] for max in c.execute("SELECT MAX(Id) FROM Patents;")][0]
print maxid