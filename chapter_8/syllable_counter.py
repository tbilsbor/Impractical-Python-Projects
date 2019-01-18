#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:29:46 2019

@author: toddbilsborough

Project 15 - Counting Syllables from Impractical Python Projects

Objective
- Write a Python program that counts the number of syllables in an
English word or phrase

Notes
- First experience with natural language processing and the corpus, so I'll
mostly be copying from the book to get a sense of how all this works
- The CMU Corpus puts a numeral in front of each vowel sound; those can
be counted to count the number of syllables
- Had to adjust the count_syllables to return None if it can't find the word
in either list

"""

import sys
from string import punctuation
import json
from nltk.corpus import cmudict

with open('missing_words.json') as f:
    MISSING_WORDS = json.load(f)
CMUDICT = cmudict.dict()

def count_syllables(words):
    """Use corpora to count syllables in English word or phrase
    Mostly copied from book"""
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_syllables = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s"):
            word = word[:-2]
        if word in MISSING_WORDS:
            num_syllables += MISSING_WORDS[word]
        elif word in CMUDICT.keys():
            for phonemes in CMUDICT[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_syllables += 1
        else:
            return
    return num_syllables

def main():
    """Counts syllables in a word or phrase
    Mostly copied from book"""
    print("Syllable Counter")
    while True:
        word = input("Enter word or phrase, enter to exit: ")
        if word == '':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print("Number of syllables in \"{}\" is: {}"
                  .format(word, num_syllables))
            print()
        except KeyError:
            print("Word not found. Try again.\n", file=sys.stderr)
            
if __name__ == '__main__':
    main()
