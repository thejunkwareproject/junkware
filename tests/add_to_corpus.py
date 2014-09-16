impoimport lockfile, tempfile, shutil

def append_line(fname, line):
    with lockfile.FileLock(fname):
        fp = open(fname, 'a+')
        fp.write(line)
        fp.write('\n')
        fp.close()

def remove_line(fname, line):
    with lockfile.FileLock(fname):
        tmp = tempfile.TemporaryFile()
        fp = open(fname, 'r+')
        # write all lines from orig file, except if matches given line
        for l in fp:
            if l.strip() != line:
                tmp.write(l)

        # reset file pointers so entire files are copied
        fp.seek(0)
        tmp.seek(0)

        # copy tmp into fp, then truncate to remove trailing line(s)
        shutil.copyfileobj(tmp, fp)
        fp.truncate()
        fp.close()
        tmp.close()

# can use these functions as follows:
from corpus import append_line, remove_line
append_line('test.txt', 'foo')
remove_line('test.txt', 'foo')
