#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:15:43 2019

@author: toddbilsborough

Route cipher encryption challenge project 
from Impractical Python Projects

Takes a given message with a given key and a given transposition
matrix and encodes it into a route transposition cipher
"""

import sys

CODE_WORDS = {
        "BATTERIES": "HOUNDS",
        "VICKSBURG": "ODOR",
        "APRIL": "CLAYTON",
        "16": "SWEET",
        "GRAND": "TREE",
        "GULF": "OWL",
        "FORTS": "BAILEY",
        "RIVER": "HICKORY",
        "25": "MULTIPLY",
        "29": "ADD",
        "ADMIRAL": "HERMES",
        "PORTER": "LANGFORD"
        }

ROWS = 7
COLS = 6

KEY = "-1 3 -2 6 5 -4"

PLAINTEXT = """We will run the batteries at Vicksburg for the night of April \
16 and proceed to Grand Gulf where we will reduce the forts. \
Be prepared to cross the river on April 25 or 29. \
Admiral Porter.""".upper()

def swap_words(plaintext):
    """Replaces words in the plaintext with the codewords"""
    for word, codeword in CODE_WORDS.items():
        plaintext = plaintext.replace(word, codeword)
    return plaintext

def validate_ciphertext(cipherlist, rows, cols):
    if len(cipherlist) != rows * cols:
        print("\nCipher length doesn't match matrix")
        print("Terminating")
        sys.exit()

def validate_key(keylist, cols):
    """Make sure the key has the right information"""
    if len(keylist) != cols:
        print("\nKey length does not match columns")
        print("Terminating")
        sys.exit()
    for c in range(1, cols + 1):
        if (c not in keylist and -c not in keylist):
            print("\nKey missing columns")
            print("Terminating")
            sys.exit()
    if any(keylist.count(str(c)) + keylist.count(str(-c)) > 1 for 
           c in range(1, cols + 1)):
        print("\nKey has duplicate columns")
        print("Terminating")
        sys.exit() 
        
def encode_matrix(ciphertext, rows, cols):
    """Turns the ciphertext into the transposition matrix"""
    transposition_matrix = []
    ciphertext = ciphertext[::-1] # Reverse for popping
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(ciphertext.pop())
        transposition_matrix.append(row)
    return transposition_matrix
    
def generate_ciphertext(transposition_matrix, key):
    """Generates the ciphertext from the transposition matrix"""
    ciphertext = ""    
    for num in key:
        c = abs(num) - 1
        if num > 0:
            for row in transposition_matrix:
                ciphertext += "{} ".format(row[c])
        elif num < 0:
            for row in transposition_matrix[::-1]:
                ciphertext += "{} ".format(row[c])
    return ciphertext

def main():
    """Prep the text. Swap the code words. Prep the key. 
    Create and encode the matrix. Generate the ciphertext. Print"""
    plaintext = PLAINTEXT.replace(".", "")
    ciphertext = swap_words(plaintext)
    # Add filler. 6 * 7 = 42 and there are 37 words so we need 5
    ciphertext += " LARRY FROZEN KINGDOM SAVANT TUMULT"
    cipherlist = ciphertext.split(" ")
    validate_ciphertext(cipherlist, ROWS, COLS)
    keylist = [int(k) for k in KEY.split(" ")]
    validate_key(keylist, COLS)
    transposition_matrix = encode_matrix(cipherlist, ROWS, COLS)        
    final_cipher = generate_ciphertext(transposition_matrix, keylist)
    print("\nPlaintext:\n")
    print(PLAINTEXT)
    print("\nCiphertext:\n")
    print(final_cipher)
    
if __name__ == '__main__':
    main()
