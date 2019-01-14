#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 00:14:02 2019

@author: toddbilsborough

Saving Mary project from
Impractical Python Projects

Objective 
- Encode a null cipher in a list of names
Encode letters in a cycle - second letter the second word
and third letter of the third word then alternating after that
"Stuart" and "Jacob" are skipped to conceal the cipher, and appear early
to better avoid detection

Process notes :

- Just picking the first words that are available as they come along would 
be obvious. They can be alphabetical, but there should be the randomness in 
the mix
- Had to look at the names file to know what I'm working with. 624 names.
The names should be equally spread out across the alphabet. The message
is 21 characters long without whitespace. I'll start with a 1 out of 15
chance for word selection and see how that does and then walk it in
- I overestimated how likely certain letters were to occur in certain
places in names. Set probability for those selections to 1 until I get
that working
- Actually even then it runs out of names. I'll have to cycle through it
- random_chance = 5 seems to give a good appearance of randomness

"""

import itertools
from random import randint
import sys

PLAINTEXT = "Give your word and we rise"

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = list(in_file.read().strip().split("\n"))
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

def check_name(letter, name, cycle):
    """Checks whether the name is a match for a given letter and cycle
    Cycle alternates between 2 and 3"""
    if cycle == 2:
        return True if name[1] == letter else False
    if cycle == 3:
        return True if name[2] == letter else False

def main():
    """Prep plaintext. Load word list. Match words according to
    cycle and toss them into the cipher string. Print."""
    # Prep plaintext, reverse for easy popping
    plaintext = list(PLAINTEXT.lower().strip().replace(" ", "")[::-1])
    names_list = itertools.cycle(load("supporters.txt"))
    cipherlist = [] # List for easy insertion of null words
    cycle = 1
    # Chance for a name to be selected if it meets all other criteria
    # Increase to increase appearance of randomness in list
    random_chance = 5 
    for name in names_list:
        if cycle == 1 and randint(1, 5) == 1:
            cipherlist.append(name)
            cycle = 2
            continue
        if (cycle == 2 and check_name(plaintext[-1], name, cycle) and
            randint(1, random_chance) == 1 and name not in cipherlist):
            cipherlist.append(name)
            plaintext.pop()
            cycle = 3
            if len(plaintext) == 0:
                break
            continue
        if (cycle == 3 and check_name(plaintext[-1], name, cycle) and
            randint(1, random_chance) == 1 and name not in cipherlist):
            cipherlist.append(name)
            plaintext.pop()
            cycle = 2
            if len(plaintext) == 0:
                break        
            continue
    # Add null words
    cipherlist.insert(randint(0, 5), "Jacob")
    cipherlist.insert(randint(0, 10), "Stuart")
    #Print
    print("\nMessage:\n")
    print(PLAINTEXT)
    print("\nNames list:\n")
    print(*cipherlist, sep="\n")
    
if __name__ == "__main__":
    main()
