"""
This module contains packaging functions.

Contents:
    - :func:`walker`: walks through directories and keeps lists of subpaths of subdirectories and full paths of files.

:author: TCHILINGUIRIAN Théo
:email: theo.tchlx@gmail.com
:date: 2023-12-15
"""


import os


def walker(path: str):
    """
    This function walks through the subdirectories from the given path and outputs a list of paths to each file in every subdirectory (from the given path argument to each file). The given directory is included.
    
    :param path: path to directory to be walked through.
    :type path: str
    
    :return: full_filenames, a list of paths to each file in every subdirectory (including the given path argument). Each path string starts relative to the given path argument.
    :rtype: list
    """

    dirpath, dirnames, filenames = [], [], []
    for triplet in os.walk(path):
        dirpath.append(triplet[0])
        dirnames.append(triplet[1])
        filenames.append(triplet[2])
    
    full_filenames = list()
    for i in range(len(dirpath)):
        for j in range(len(filenames[i])):
            full_filenames.append(os.path.join(dirpath[i], filenames[i][j]))
    
    return dirpath, dirnames, filenames
