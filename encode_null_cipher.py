#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:19:33 2019

@author: toddbilsborough

Writing a Null Cipher (Project #11) project
From Impractical Python Projects

Object: Write code that hides a null cipher within a list of words
"""

from load_dictionary import load
import random

#=============================================================================
# USER INPUT

# File containing the cipher
PLAINTEXT = "Panel at east end of chapel slides"

# Number of letters into a word to place cipher letter
LETTERS_AFTER = 3

# END USER INPUT
#=============================================================================

def main():
    """load word list. prep text. look for words to put them in
    and add them to the list. print"""
    dictionary = load("words.txt")
    word_list = []
    plaintext = list(PLAINTEXT.lower().strip().replace(" ", ""))
    letters_after = LETTERS_AFTER - 1 # Align to 0-index
    temp_list = []
    for word in (w for w in dictionary if len(w) > LETTERS_AFTER):
        if word[letters_after] == plaintext[0]:
            temp_list.append(word)
        if len(temp_list) == 10:
            word_list.append(random.choice(temp_list))
            temp_list.clear()
            plaintext.pop(0)
            if len(plaintext) == 0:
                break
    if len(plaintext) > 0:
        print("Couldn't find enough words!")
        return
    print("\nPlaintext\n")
    print(PLAINTEXT)
    print("\nEncoded as vocabulary list\n")
    print(*word_list, sep="\n")
    
if __name__ == '__main__':
    main()
