#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:11:41 2019

@author: toddbilsborough

Encryption half of the rail fence cipher encryption/decryption project
in Impractical Python Projects

Objective: Design a user-friendly program that will encrypt
plain text via rail fence encryption.

INFORMATION REQUIRED

1. The text to be encrypted

USER INSTRUCTIONS

1. Enter information in USER INPUT section
2. Run program
"""

#=============================================================================
# USER INPUT

# Text to be encrypted, in triple quotes
PLAINTEXT = """Buy more Maine potatoes"""

# END USER INPUT
#=============================================================================

def encrypt(plaintext):
    """Prepare the text and execute the encryption"""
    pt = plaintext.upper().replace(" ", "")
    upper = pt[0::2]
    lower = pt[1::2]
    intertext = upper + lower
    ciphertext = ""
    for i in range(0, len(intertext)):
        if i != 0 and i % 5 == 0:
            ciphertext += " {}".format(intertext[i])
        else:
            ciphertext += intertext[i]
    return ciphertext

def main():
    """Run the encryption subroutine and print the results"""
    ciphertext = encrypt(PLAINTEXT)

    print("\nPLAINTEXT:\n")
    print(PLAINTEXT + "\n")
    print("ENCRYPTED TEXT:\n")
    print(ciphertext + "\n")

if __name__ == '__main__':
    main()
