#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:29:46 2019

@author: toddbilsborough

Project 15 - Counting Syllables from Impractical Python Projects
Subproject - Missing words finder

Objective
- (overall) Write a Python program that counts the number of syllables in an
English word or phrase
- This program finds words missing from the CMU corpus and creates a 
dictionary of the missing words and their syllable counts

Notes
- Ignored some of the error correction; this is for me to create a syllable
exception dictionary, and that file will be available in the repository


"""

import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict() # Carnegie Mellon University Pronouncing Dictionary

def load_haiku(filename):
    """Open and return training corpus of haiku as a set.
    Mostly copied from book"""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split())
        return haiku
    
def cmudict_missing(word_set):
    """Find and return words in word set missing from cmudict.
    Mostly copied from book"""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nExceptions: ")
    print(*exceptions, sep='\n')
    print("\nNumber of unique words in haiku corpus = {}"
          .format(len(word_set)))
    print("Number of words in corpus not in cmudict = {}"
          .format(len(exceptions)))
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print("CMUdict membership = {:.1f}{}".format(membership, '%'))
    return exceptions

def make_exceptions_dict(exceptions_set):
    """Return dictionary of words and syllable counts from a set of words
    Mostly copied from book, left out some of the error correcting stuff
    for now"""
    missing_words = {}
    print("Input number of syllables in word")
    for word in exceptions_set:
        while True:
            num_syllables = input("Enter number syllables in {}, x to exit: "
                                  .format(word))
            if num_syllables == 'x':
                sys.exit()
            if num_syllables.isdigit():
                break
        missing_words[word] = int(num_syllables)
        print()
        pprint.pprint(missing_words, width=1)
    return missing_words

def save_exceptions(missing_words):
    """Save exceptions dictionary as json file"""
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")

def main():
    """Loads the training text. Finds exceptions. Makes a dictionary of
    the words and their syllables. Saves.
    Mostly copied from book"""
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    missing_words_dict = make_exceptions_dict(exceptions)
    save_exceptions(missing_words_dict)

if __name__ == '__main__':
    main()
