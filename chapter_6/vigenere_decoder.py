#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:20:11 2019

@author: toddbilsborough

Not a project from the book, but if I'm going to make an encoder,
might as well make a decoder!

The Vigenere decoder takes a string encoded with a Vigenere cipher
and decodes it using a given key

"""

from itertools import cycle
import vigenere_cipher_encoder as vce

#=============================================================================
# USER INPUT

CIPHERTEXT = "Lwtw vv i mmuryf etdwnjm"
KEY = "splendiferous"

# END USER INPUT
#=============================================================================

def decode_vigenere(ciphertext, key):
    """Decode a vigenere-encoded ciphertext using a given key"""
    table = vce.generate_vigenere_table()
    key_cycle = cycle(list(key))
    plaintext = ""
    for char in ciphertext:
        c = char.lower()
        if char == " ":
            plaintext += " "
            continue
        if char.isupper():
            for key, value in table[next(key_cycle)].items():
                if value == c:
                    plaintext += key.upper()
                    break
            continue
        if char.islower():
            for key, value in table[next(key_cycle)].items():
                if value == c:
                    plaintext += key.lower()
                    break
            continue
    return plaintext
        
def main():
    """Decode and print"""
    plaintext = decode_vigenere(CIPHERTEXT, KEY)
    print("\nCiphertext:\n")
    print(CIPHERTEXT)
    print("\nPlaintext:\n")
    print(plaintext)
    
if __name__ == '__main__':
    main()
