#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:26:06 2019

@author: toddbilsborough

Load a text file as a list.

Arguments:
    -text file name (and directory path, if needed)
    
Exceptions:
    -IOError if filename not found.
    
Returns:
    -A list of all words in a text file in lower case
    
Requires: sys
"""

import sys

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt if len(x) > 1]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)