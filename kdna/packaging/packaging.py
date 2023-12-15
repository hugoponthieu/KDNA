"""
This module contains packaging functions.

Contents:
    - :func:`russian_doll`: .
    - :func `packager`: .

:author: TCHILINGUIRIAN Théo
:email: theo.tchlx@gmail.com
:date: 2023-12-15
"""


import os
import zipfile
from auxtools import auxtools

###
def russian_doll(path):
    # encrypt then zips from the bottom of the tree, then goes up and does the same up to tree root.
    pass
###

def dir_packager(path, out):
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zipf:
        dirpath, dirnames, filenames = auxtools.walker(path)
        for filepath in filenames:
            arcname = os.path.relpath(filepath, path)
            zipf.write(filepath, arcname)


def file_packager(path):
    """
    """



