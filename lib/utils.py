#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import unicodedata
import re


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """

    if type(value) is str:
        value = value.decode('utf-8')

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '_', value))

    return value


def list_to_csv(keys, rows, csv_filepath):
    ''' Store a list into a CSV file'''
    with open(csv_filepath, 'w') as f:  # writes the final output to CSV
        csv_out = csv.writer(f)
        csv_out.writerow(keys)  # add header
        for row in rows:
            csv_out.writerow(row)
    print " csv has been stored as %s" % csv_filepath


def nx_to_gephi_csv(nx_graph, name, dir_path):
    ''' Store a NetworkX graph object into CSV files (edges+nodes) for Gephi'''
    list_to_csv(["Id", "Label"], nx_graph.nodes(),
                dir_path + '/' + name + '_nodes.csv')
    list_to_csv(["Source", "Target"], nx_graph.edges(),
                dir_path + '/' + name + '_edges.csv')
    print "graph files (nodes+edges) saved at %s" % dir_path


def write_json_file(data, myfile):
    """Store a  dict into a JSON file """
    import io
    import json
    with io.open(myfile, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


def nx_to_gv_file(nx_graph, name, dir_path):
    ''' Convert  to Graphviz file '''
    # t0=time()

    #
    gv_filepath = dir_path + "/" + name + ".gv"
    viz_filepath = dir_path + "/" + name + ".png"

    with open(gv_filepath, 'w') as f:

        line = "digraph mentions {\n"  # open .gv file
        f.write(line)

        for edge in nx_graph.edges():
            line = '"' + edge[0] + '"' + "->" + '"' + edge[1] + '"' + "\n"
            # print line
            f.write(line)

        line = "}" + "\n"  # close .gv file
        f.write(line)

    print " graphiz file saved as %s" % gv_filepath

    # draw with graphviz
    command = "sfdp -Gbgcolor=black -Ncolor=white -Ecolor=white -Nwidth=0.05  -Nheight=0.05 -Nfixedsize=true -Nlabel='' -Earrowsize=0.4 -Gsize=75 -Gratio=fill -Tpng " + gv_filepath + " > " + viz_filepath

    os.system(command)
    print "viz graph saved as %s" % viz_filepath
