#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:19:51 2019

@author: toddbilsborough

Chapter 8 practice project from Impractical Python Projects

Objective
- Write a program that uses the syllable_counter to analyze the number
of syllables in random dictionary words

Notes
- Doesn't work great with the large dictionary file I'm using. 
It finds maybe 1 word in 5. 
If I were implementing this I'd write in a subroutine to prompt for manual
input of syllables when one isn't found

"""

import sys
import syllable_counter as sc
import random

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
        
def main():
    """Load the dictionary. Ask for number of words to count. Create
    the list of words. Print."""
    dict_file = load('words.txt')
    num_words = int(input("\nNumber of words to check: "))
    words_count_list = {}
    for n in range(0, num_words):
        word = random.choice(dict_file)
        if word not in words_count_list.keys():
            count = sc.count_syllables(word)
            if count == None:
                words_count_list[word] = "not found"
            else:
                words_count_list[word] = count
    for word, count in words_count_list.items():
        print("{}: {}".format(word, count))
    
if __name__ == '__main__':
    main()
