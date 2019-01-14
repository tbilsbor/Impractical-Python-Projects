#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:47:00 2019

@author: toddbilsborough

Colchester Catch practice project from
Impractical Python Projects (chapter 5)

Objective
- Write a python program that takes an input n and checks for and
displays a null cipher based on the nth letter after the start of every 
nth word.

"""

import sys

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = list(in_file.read().strip().replace("\n", "")\
                              .replace("  ", " ").split(" "))
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

def main():
    """Load message, get input for n value, loop through and add letters,
    print"""
    message = load("colchester_message.txt")
    running = True
    while running:
        n = input("Value to check (# to exit): ")
        if n == "#":
            break
        n = int(n)
        plaintext = ""
        for i, word in enumerate(message):
            if (i + 1) % n == 0:
                plaintext += word[n - 1]
        print("\nN value = {}\n".format(n))
        print(plaintext)
        
if __name__ == '__main__':
    main()
