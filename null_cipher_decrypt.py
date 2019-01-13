#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:47:41 2019

@author: toddbilsborough

Trevanion cipher decryption project (project #10)
from Impractical Python Projects

Objective: Write code that finds the letters hidden after punctuation
marks in a null cipher and lets the user choose the number of letters after
a punctuation mark to search for a solution
"""

import sys
import string

#=============================================================================
# USER INPUT

# File containing the cipher
FILE = "trevanion.txt"

# Number of letters after a punctuation mark to search
LETTERS_AFTER = 3

# END USER INPUT
#=============================================================================

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip()
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

def main():
    """Load file. Prep file (strip of whitespace. Solve cipher. Print"""
    cipher = load(FILE)
    ciphertext = cipher.replace(" ", "")
    ciphertext = ciphertext.replace("\n", "")
    plaintext = ""
    counting = False
    count = 0
    for char in ciphertext:
        if counting:
            count += 1
        if count == 3:
            plaintext += char
        if char in string.punctuation:
            counting = True
            count = 0
    
    print("\nNull Cipher:\n")
    print(cipher)
    print("\nPlaintext:\n")
    print(plaintext)
    
if __name__ == '__main__':
    main()
