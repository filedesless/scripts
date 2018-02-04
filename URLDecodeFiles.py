#!/usr/bin/env python3

# rename all files in the current folder
# and sub-folders to human readable name
# from an URL-encoded filename

import os
from urllib.parse import unquote

for dirpath, dnames, fnames in os.walk("."):
    for fname in fnames:
        oldname = "{}/{}".format(dirpath, fname)
        newname = "{}/{}".format(dirpath, unquote(fname))
        print(oldname, newname)
        os.rename(oldname, newname)
