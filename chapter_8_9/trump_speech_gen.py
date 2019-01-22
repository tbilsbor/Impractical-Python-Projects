#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:43:42 2019

@author: toddbilsborough

Uses the functions from the haiku generator and training files from 
trump tweets and speeches to generate Trump-talk

ToDo
- More text in the training files
"""

import json
import random
import sys
from string import punctuation
import haiku_gen_improved as hg

def load_tweets(file):
    """Loads the json file containing trump tweet data"""
    with open(file) as f:
        data = json.load(f)
    return data

def print_text(text):
    """Prints out the current text"""
    print_string = ""
    for word in text:
        print_string += "{} ".format(word)
    print(print_string)
    
def strip_punctuation(word_list):
    """Strips all words in a list of punctuation"""
    return [word.strip(punctuation) for word in word_list]

def add_punctuation(word):
    """Prompts user to input punctuation into the text"""
    punct = "a"
    while punct not in punctuation:
        punct = input("Punctuation: ")
    return "{}{}".format(word, punct)
    
def word_after_one(word, dictionary):
    """Return all acceptable words in a corpus that follow a given word"""
    accepted_words = []
    options = dictionary.get(word)
    if options != None:
        accepted_words = [w for w in options]
    return accepted_words

def word_after_two(word_pair, dictionary):
    """Return all acceptable words in a corpus that follow
    a given word pair"""
    accepted_words = []
    options = dictionary.get(word_pair)
    if options != None:
        accepted_words = [w for w in options]
    return accepted_words

def select_word(options):
    """Randomly offer 10 words from the options. User selects one.
    Returns that word"""
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
    if choice == 'p':
        choice = input("Word selection: ")
        word = selection[int(choice) - 1]
        return add_punctuation(word)
    choice = int(choice) - 1
    word = selection[choice]
    return word

def main():
    """Interactively generates a Trump speech using Markov chains"""
    # Load and prep training files
    raw_speech_text = hg.load_training_file('trump_train.txt')
    speech_text = hg.prep_training(raw_speech_text)
    tweet_data = load_tweets('trump_tweets.json')
    raw_tweets = ""
    for dct in tweet_data:
        raw_tweets += "{} ".format(dct['text'])
    tweets = hg.prep_training(raw_tweets)
    corpus = speech_text + tweets
    corpus = strip_punctuation(corpus)
    dict_1 = hg.map_one_to_one(corpus)
    dict_2 = hg.map_two_to_one(corpus)
    text = []
    
    # Introduction
    print("\nTrump Speech Generator\n")
    print("Select words to add to speech")
    print("\'x\' to exit")
    print("\'p\' to add punctuation")
    print("Select \'p\' before selecting the word you want to punctuate")

    # Select first word
    options = corpus
    print ()
    selection = select_word(corpus)
    text.append(selection)
    
    # Select second word
    last = text[0]
    options = word_after_one(last, dict_1)
    print_text(text)
    selection = select_word(options)
    text.append(selection)
        
    # Select subsequent word
    while True:
        last = "{} {}".format(text[-2].strip(punctuation),
                text[-1].strip(punctuation))
        options = word_after_two(last, dict_2)
        if options == []:
            last = last.split()[1]
            options = word_after_one(last, dict_1)
            while options == []:
                last = random.choice(corpus)
                options = word_after_one(last, dict_1)
        print_text(text)
        selection = select_word(options)
        text.append(selection)
        
    print_text(text)
    
if __name__ == '__main__':
    main()
