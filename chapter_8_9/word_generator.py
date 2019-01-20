#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:44:41 2019

@author: toddbilsborough

New Word Generator challenge project from Impractical Python Projects ch 9

Objective
- Use a dictionary as a training file to build new words from Markov chains

Notes
- These chains are going to be huge and will probably take a while to
generate. Probably best to pre-generate them and save the data
    - Actually much faster than I expected, but I'm leaving it as is

ToDo
- Create corpora for first and last letters
- Compare words against a dictionary file to avoid returning real words
"""

import json
import random
import string
import sys
from collections import defaultdict
from haiku_generator import load_training_file, prep_training

def create_chains(corpus, order):
    """Generate Markov chains from a dictionary file"""
    chains = defaultdict(list)
    for word in corpus:
        if len(word) < order + 1:
            continue
        for i in range(len(word) - order):
            letters = word[i:i+order]
            next_letter = word[i+order]
            chains[letters].append(next_letter)
    return chains

def load_chains(corpus, order):
    """Load the chains from file, create if they don't exist"""
    file = "order_{}_chains.json".format(order)
    try:
        with open(file) as f:
            chains = json.load(f)
    except:
        inp = None
        while inp != 'y' and input != 'n':
            inp = input("Order {} chain not found. Create? "
                        .format(order)).lower()
        if inp == 'n':
            print("Cannot continue without file")
            print("Terminating")
            sys.exit()
        chains = create_chains(corpus, order)
        json_string = json.dumps(chains)
        f = open(file, 'w')
        f.write(json_string)
        f.close()
    return chains

def generate_word(chains):
    """Generate a new word using the chains"""
    length = random.randint(3, 10)
    word = random.choice(string.ascii_lowercase)
    while len(word) < length:
        order = len(word) if len(word) < 4 else 4
        options = []
        while len(options) == 0:
            last = word[-order:]
            try:
                options = chains[order-1][last]
            except KeyError:
                order -= 1
        nxt = random.choice(options)
        word += nxt
    return word

def main():
    """Load the corpus, load chain dictionaries, generate words"""
    # Preparation
    corpus = load_training_file('words.txt')
    corpus = prep_training(corpus)
    
    # Loading
    chains = []
    for n in range(1, 5):
        chains.append(load_chains(corpus, order=n))
    
    # Generate words in a user interface loop
    print("\nNew word generator\n")
    while True:
        num_words = input("How many words? \'x\' to exit: ")
        if num_words == 'x':
            sys.exit()
        num_words = int(num_words)
        for n in range(num_words):
            new_word = generate_word(chains)
            print(new_word)

if __name__ == '__main__':
    main()
