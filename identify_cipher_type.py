#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:11:40 2019

@author: toddbilsborough

Identifying Cipher Types practice project from
Impractical Python Projects

Objective: Determine whether a given ciphertext is a transposition
cipher or a substitution cipher by comparing letter frequency
to that of general English

Strategy: The letters with the greatest and the least frequencies are
the ones most likely to differ in a substitution cipher. So I'll take
the most six frequent and the least six frequent letters and compare
their expected occurence against the ciphertext

Conclusion: The letter frequency of cipher_a is close to expected values
and is thus likely to be a transposition cipher. The letter frequency of
cipher_b differs significantly and is more likely a substitution cipher

Data on letter frequencies from 
http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

Cipher text files from
https://github.com/rlvaugh/Impractical_Python_Projects

"""

import sys

FREQUENCY = {
        'e': 0.12702,
        't': 0.09056,
        'a': 0.08167,
        'o': 0.07507,
        'i': 0.06966,
        'n': 0.06749,
        'v': 0.00978,
        'k': 0.00772,
        'j': 0.00153,
        'x': 0.00150,
        'q': 0.00095,
        'z': 0.00074
        }

def load_ciphertext(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip()
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

def analyze_frequency(ciphertext):
    """Analyze the frequency of letters in the ciphertext"""
    analysis = {}
    for letter, _ in FREQUENCY.items():
        analysis[letter] = ciphertext.count(letter) / len(ciphertext)
    return analysis

def main():
    """Load the text, analyze the frequency, print out comparison
    to expected values"""
    ciphertext = load_ciphertext('cipher_b.txt').lower()
    analysis = analyze_frequency(ciphertext)
    for letter, value in FREQUENCY.items():
        expected = "{0:.5f}".format(value)
        found = "{0:.5f}".format(analysis[letter])
        diff = "{0:.5f}".format(value - analysis[letter])
        print("{} - Expected: {} Found: {} Diff: {}".format(letter, 
              expected, found, diff))
        
if __name__ == '__main__':
    main()
