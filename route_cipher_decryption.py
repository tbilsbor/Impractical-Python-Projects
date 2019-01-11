#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:27:58 2019

@author: toddbilsborough

Route cipher decription project from
Impractical Python Projects

Objective: Design a user-friendly program that will decrypt
a route cipher based on an assumed encryption matrix and path.

INFORMATION REQUIRED

1. The text to be decrypted
2. The number of rows and columsn in the transposition matrix
3. The key

The key is a series of numbers representing all of the columns
in the transposition matrix. The columns are read in the order that
they appear in the key. If the number is positive, the column is
read from top to bottom. If the number is negative, the column
is read from bottom to top.

USER INSTRUCTIONS

1. Enter information in USER INPUT section
2. Run program
"""

import sys

#=============================================================================
# USER INPUT

# String to decrypt (in triple quotes)
CIPHERTEXT = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT \
WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"""

# Number of columns in transposition matrix
COLS = 4

# Number of rows in transposition matrix
ROWS = 6

# Key: Column numbers in the order they are to be read
# Positive for reading down, negative for reading up
KEY = """-1 2 -3 4"""

# END OF USER INPUT
#=============================================================================

def decrypt(rows, key, cipherlist):
    """Process the actual decryption"""
    translation_matrix = []
    translation_string = ""
    for number in key:
        number = int(number)
        start = (abs(number) - 1) * ROWS
        end = start + rows
        row = cipherlist[start:end]
        if number > 0:
            row = row[::-1]
        translation_matrix.append(row)
    for _ in range(rows):
        for row in translation_matrix:
            translation_string += "{} ".format(str(row.pop()))
    return translation_string

def validate_cols_rows(cipherlist):
    """Verify that columns and rows make sense with ciphertext length"""
    if COLS * ROWS != len(cipherlist):
        print("\nColumns and rows do not match cipher length")
        print("Terminating")
        sys.exit()
        
def validate_key(keylist):
    """Make sure the key has the right information"""
    if len(keylist) != COLS:
        print("\nKey length does not match columns")
        print("Terminating")
        sys.exit()
    for c in range(1, COLS + 1):
        if (str(c) not in keylist and str(-c) not in keylist):
            print("\nKey missing columns")
            print("Terminating")
            sys.exit()
    if any(keylist.count(str(c)) + keylist.count(str(-c)) > 1 for 
           c in range(1, COLS + 1)):
        print("\nKey has duplicate columns")
        print("Terminating")
        sys.exit()        

def main():
    """Decrypt and print encrypted text based on provided values"""
    cipherlist = CIPHERTEXT.split(" ")
    validate_cols_rows(cipherlist)
    keylist = KEY.split(" ")
    validate_key(keylist)
    translation_string = decrypt(ROWS, keylist, cipherlist)

    print("\n")
    print("ENCRYPTED TEXT:\n")
    print(CIPHERTEXT + "\n")
    print("Rows = {} Cols = {} Key = {}\n".format(ROWS, COLS, KEY))
    print("PLAINTEXT:\n")
    print(translation_string)

if __name__ == '__main__':
    main()
