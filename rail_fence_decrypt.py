#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:34:26 2019

@author: toddbilsborough

Decryption half of the rail fence cipher encryption/decryption project
in Impractical Python Projects

Objective: Design a user-friendly program that will decrypt
ciphertext encrypted via rail fence encryption.

INFORMATION REQUIRED

1. The text to be decrypted

USER INSTRUCTIONS

1. Enter information in USER INPUT section
2. Run program
"""

import math

#=============================================================================
# USER INPUT

# Ciphertext, in triple quotes
# Insert a backslash before new lines
CIPHERTEXT = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT \
ES"""

# END USER INPUT
#=============================================================================

def prep_ciphertext(ciphertext):
    """Remove whitespace"""
    ciphertext = ciphertext.replace(" ", "")
    return ciphertext

def split_rails(ciphertext):
    """Split message into the two rails"""
    row_1_len = math.ceil(len(ciphertext)/2)
    row1 = ciphertext[:row_1_len]
    row2 = ciphertext[row_1_len:]
    return row1, row2

def decrypt(row1, row2):
    """Decrypt the message"""
    plaintext = ""
    for i in range(len(row1)):
        plaintext += row1[i]
        if i < len(row2): # Row 1 might have 1 more letter
            plaintext += row2[i]
    return plaintext

def main():
    """Prep the ciphertext, split the rows, decrypt, print"""
    ciphertext = prep_ciphertext(CIPHERTEXT)
    row1, row2 = split_rails(ciphertext)
    plaintext = decrypt(row1, row2)
    print("\nCiphertext:\n")
    print(CIPHERTEXT + "\n")
    print("\nPlaintext:\n")
    print(plaintext + "\n")
    
if __name__ == '__main__':
    main()
