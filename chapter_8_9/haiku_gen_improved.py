#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:48:06 2019

@author: toddbilsborough

Based on Project #16 from Impractical Python Projects

Objective
- Interactively write haiku based on a Markov chain training corpus

Notes
- This version is indeed more fun and generates better haiku

"""

import random
import sys
from collections import defaultdict
from syllable_counter import count_syllables

def load_training_file(file):
    """Load file and return text as string"""
    with open(file) as f:
        text = f.read()
        return text

def prep_training(raw_haiku):
    """Remove newline, split words on spaces, return list"""
    corpus = raw_haiku.replace('\n', ' ').split()
    return corpus

def map_one_to_one(corpus):
    """Parse the corpus and map words to the word that follows"""
    dictionary = defaultdict(list)
    for index, word in enumerate(corpus[:len(corpus) - 1]):
        dictionary[word].append(corpus[index + 1])
    return dictionary

def map_two_to_one(corpus):
    """Parse the corpus and map words to the word that follows"""
    dictionary = defaultdict(list)
    for index, word in enumerate(corpus[:len(corpus) - 2]):
        dictionary[word + ' ' + corpus[index + 1]].append(corpus[index + 2])
    return dictionary

def random_word(corpus):
    """Return a random word and syllable count from the corpus"""
    syllables = 5
    while syllables > 4:
        word = random.choice(corpus)
        syllables = count_syllables(word)
    return (word, syllables)

def word_after_one(word, dictionary, current_syllables, target_syllables):
    """Return all acceptable words in a corpus that follow a given word"""
    accepted_words = []
    options = dictionary.get(word)
    if options != None:
        accepted_words = [w for w in options if
                          current_syllables + count_syllables(w) <=
                          target_syllables]
    return accepted_words

def word_after_two(word_pair, dictionary, current_syllables,
                   target_syllables):
    """Return all acceptable words in a corpus that follow
    a given word pair"""
    accepted_words = []
    options = dictionary.get(word_pair)
    if options != None:
        accepted_words = [w for w in options if
                          current_syllables + count_syllables(w) <=
                          target_syllables]
    return accepted_words

def select_word(options):
    """Randomly offer 10 words from the options. User selects one.
    Returns that word and its syllable count"""
    options = list(set(options)) # Remove duplicate words
    selection = []
    if len(options) > 10:
        for n in range(10):
            word = random.choice(options)
            while word in selection:
                word = random.choice(options)
            selection.append(word)
    else:
        selection = options
    # Print selection options
    for n in range(len(selection)):
        index = n + 1
        print("{}. {}".format(index, selection[n]))
    choice = input("Choice: ")
    if choice == 'x':
        sys.exit()
    choice = int(choice) - 1
    word = selection[choice]
    syllables = count_syllables(word)
    return word, syllables

def print_haiku(haiku):
    """Prints the current haiku"""
    print("Current haiku:\n")
    for line in haiku:
        if line != []:
            line_string = " ".join(line)
            print(line_string)
    print()

def main():
    """Load the corpus and the dictionaries, then build the haiku"""
    print("\nHaiku generator\n")
    print("Enter x at any prompt to exit\n")

    # Loading and preparation
    corpus = load_training_file('train.txt')
    corpus = prep_training(corpus)
    dict_1 = map_one_to_one(corpus)
    dict_2 = map_two_to_one(corpus)
    target_syllables = [5, 7, 5]
    
    while True:
        # Further preparations
        haiku = [[] for l in range(3)]
        current_syllables = [0 for l in range(3)]

        # Select first word
        options = corpus
        print ()
        selection, syllables = select_word(corpus)
        haiku[0].append(selection)
        current_syllables[0] += syllables
        
        # Select second word
        last = haiku[0][0]
        options = word_after_one(last, dict_1, current_syllables[0],
                                 target_syllables[0])
        print_haiku(haiku)
        selection, syllables = select_word(options)
        haiku[0].append(selection)
        current_syllables[0] += syllables
        
        # Select subsequent word
        for line in range(3):
            while current_syllables[line] < target_syllables[line]:
                if len(haiku[line]) == 0:
                    last = "{} {}".format(haiku[line-1][-2],
                            haiku[line-1][-1])
                elif len(haiku[line]) == 1:
                    last = "{} {}".format(haiku[line-1][-1], haiku[line][0])
                else:
                    last = "{} {}".format(haiku[line][-2], haiku[line][-1])
                options = word_after_two(last, dict_2,
                                         current_syllables[line],
                                         target_syllables[line])
                if options == []:
                    last = last.split()[1]
                    options = word_after_one(last, dict_1,
                                             current_syllables[line],
                                             target_syllables[line])
                    while options == []:
                        last = random.choice(corpus)
                        options = word_after_one(last, dict_1,
                                             current_syllables[line],
                                             target_syllables[line])
                print_haiku(haiku)
                selection, syllables = select_word(options)
                haiku[line].append(selection)
                current_syllables[line] += syllables
        
        print_haiku(haiku)
        rep = input("Again? ").lower()
        if rep == 'n':
            break
    
if __name__ == '__main__':
    main()
