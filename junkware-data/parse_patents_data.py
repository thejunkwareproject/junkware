#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3

conn_patdesc = sqlite3.connect('./data/old_patdesc.sqlite3')
patdesc = conn_patdesc.cursor()

conn_patdesc_ok = sqlite3.connect('./data/Patents.sqlite3')
patdesc_ok = conn_patdesc_ok.cursor()

number_of_results=10000

print "create new patent table with id"
patdesc_ok.execute('''CREATE TABLE IF NOT EXISTS Patents(
    Id integer primary key autoincrement,
    Patent text , 
    Title text,
    Description text);''')


print "read data"
i=0
for row in patdesc.execute("SELECT * FROM patdesc WHERE (abstract!='') LIMIT "+number_of_results):
    patdesc_ok.execute("INSERT INTO Patents(Patent, Title, Description) VALUES (?,?,?)", (row[0],row[1],row[2]))
    conn_patdesc_ok.commit()
    i+=patdesc_ok.rowcount

print i + " results written in the db"