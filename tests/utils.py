
import sys
import os
import glob
import re
import pydef


tags = {}


def get_cursor(tag):
    if tags:
        r = tags.get(tag)
        if not r:
            raise Exception('No tag: ' + tag)
        return r

    for name in glob.glob(os.path.join(get_sample_root(), '**/*.py'), recursive=True):
        for i, s in enumerate(open(name)):
            r = re.search(r'#\s*(\@[\w\d_\.]+)', s)
            if r:
                tags[r.groups()[0]] = (name, i)

    assert tags
    return get_cursor(tag)


def get_sample_root():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample')


def goto(word, tag):
    filename, row = get_cursor(tag)
    line = open(filename).readlines()[row]
    col = line.index(word) + len(word) - 1

    path = [get_sample_root()] + sys.path
    filename = os.path.join(get_sample_root(), filename)

    return pydef.goto_definition(path, filename, row, col, source=None)


def assert_pos(tag, b):
    filename, row = get_cursor(tag)
    assert filename == b.filename and row == b.row
