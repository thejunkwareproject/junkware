#!/bin/bash

max_pages=20
path=ftp://ftp.wwpdb.org/pub/pdb/data/biounit/coordinates/divided/

for i in $(seq $max_pages $END)
do
    if [ $i -lt 10 ] 
        then echo ${path}0$i/*
    else
        echo $path$i/*
    fi
    wget -r $path
done

gzip -d *.gz 
