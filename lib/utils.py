#!/usr/bin/env python
# -*- coding: utf-8 -*-

def progress_bar(progress):
    print '\r[{0}] {1}'.format('#'*(progress/10), progress)

def slugify(value):
    import unicodedata
    import re

    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value
    if type(value) is str:
        value=value.decode('utf-8');

    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '_', value))

    return value

def write_json_file(data,_file,):
    import io, json
    with io.open(_file, 'w', encoding='utf-8') as f:
      f.write(unicode(json.dumps(data, ensure_ascii=False)))