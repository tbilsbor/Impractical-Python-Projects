#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:29:30 2019

@author: toddbilsborough

Project #16: Markov Chain Analysis from Impractical Python Projects

Objective
- Write a program that generates haiku using Markov chain analysis.
- Allow the user to modify the haiku by independently regenerating
lines two and three

Notes
- Given the general idea of a Markov chain, everything is pretty
straight-forward, so I've just been looking at what functions are needed
and writing them myself
- The possibility of the first line just being one five syllable word
requires a lot of finagling in the rest of the program. Much more
straightforward if the first line is restricted to at least two words
- functions are good, main is a bit messy and would probably be best
if rewritten from the ground up
"""

import logging
import random
from collections import defaultdict
from syllable_counter import count_syllables

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

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
    logging.debug("map_one_to_one results for \"sake\" = %s\n",
                  dictionary['sake'])
    return dictionary

def map_two_to_one(corpus):
    """Parse the corpus and map words to the word that follows"""
    dictionary = defaultdict(list)
    for index, word in enumerate(corpus[:len(corpus) - 2]):
        dictionary[word + ' ' + corpus[index + 1]].append(corpus[index + 2])
    logging.debug("map_two_to_one results for \"sake\" = %s\n",
                  dictionary['sake'])
    return dictionary

def random_word(corpus):
    """Return a random word and syllable count from the corpus"""
    syllables = 5
    while syllables > 4:
        word = random.choice(corpus)
        syllables = count_syllables(word)
    logging.debug("random word & syllables = %s %s\n", word, syllables)
    return (word, syllables)

def word_after_one(word, dictionary, current_syllables, target_syllables):
    """Return all acceptable words in a corpus that follow a given word"""
    accepted_words = []
    options = dictionary.get(word)
    if options != None:
        accepted_words = [w for w in options if
                          current_syllables + count_syllables(w) <=
                          target_syllables]
    logging.debug("accepted words after \"%s\" = %s\n", word,
                  set(accepted_words))
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
    logging.debug("accepted words after \"%s\" = %s\n", word_pair,
                  set(accepted_words))
    return accepted_words

def main():
    """Load the corpus and the dictionaries, then build the haiku"""

    # Loading and preparation
    corpus = load_training_file('train.txt')
    corpus = prep_training(corpus)
    dict_1 = map_one_to_one(corpus)
    dict_2 = map_two_to_one(corpus)
    haiku = [[] for l in range(3)]
    syllables = [0 for l in range(3)]
    target_syllables = [5, 7, 5]

    # Build the first line
    # Select the first word
    next_word, syls = random_word(corpus)
    haiku[0].append(next_word)
    syllables[0] = syls
    logging.debug("first word & syllables = %s %s", haiku[0][0], syllables[0])
    # Then get the second from the 1-to-1 corpus
    last_word = haiku[0][0]
    options = word_after_one(last_word, dict_1, syllables[0],
                             target_syllables[0])
    next_word = random.choice(options)
    haiku[0].append(next_word)
    syllables[0] += count_syllables(next_word)
    logging.debug("second word & syllables = %s %s", next_word, syllables[0])
    # Complete the line
    while syllables[0] < 5:
        last_words = "{} {}".format(haiku[0][-2], haiku[0][-1])
        options = word_after_two(last_words, dict_2, syllables[0],
                                 target_syllables[0])
        while len(options) == 0:
            index = random.randint(0, len(corpus) - 2)
            last_words = "{} {}".format(corpus[index], corpus[index+1])
            logging.debug("empty list, new words are %s", last_words)
            options = word_after_two(last_words, dict_2, syllables[0],
                                     target_syllables[0])
        next_word = random.choice(options)
        haiku[0].append(next_word)
        syllables[0] += count_syllables(next_word)
        logging.debug("next word & syllables = %s %s", next_word, 
                      syllables[0])

    # Build the next two lines in a loop
    running = True
    while running:
        for i in range(1, 3):
            last_words = "{} {}".format(haiku[i-1][-2], haiku[i-1][-1])
            while syllables[i] < target_syllables[i]:
                options = word_after_two(last_words, dict_2, syllables[i],
                                         target_syllables[i])
                while len(options) == 0:
                    index = random.randint(0, len(corpus) - 2)
                    last_words = "{} {}".format(corpus[index],
                                  corpus[index+1])
                    logging.debug("empty list, new words are %s", last_words)
                    options = word_after_two(last_words, dict_2, syllables[i],
                                             target_syllables[i])
                next_word = random.choice(options)
                haiku[i].append(next_word)
                syllables[i] += count_syllables(next_word)
                if len(haiku[i]) == 1:
                    last_words = "{} {}".format(haiku[i-1][-1], haiku[i][0])
                else:
                    last_words = "{} {}".format(haiku[i][-2], haiku[i][-1])
        haiku_string = ""
        for line in haiku:
            for index, word in enumerate(line):
                if index == len(line) - 1:
                    haiku_string += "{}\n".format(word)
                else:
                    haiku_string += "{} ".format(word)
        print("\nHaiku:\n")
        print(haiku_string)
        regen = ''
        while regen != 'y' and regen != 'n':
            regen = input("Regenerate last two lines? ").lower()
        if regen == 'n':
            running = False
        elif regen == 'y':
            haiku = [haiku[0], [], []]
            syllables = [syllables[0], 0, 0]

if __name__ == '__main__':
    main()
