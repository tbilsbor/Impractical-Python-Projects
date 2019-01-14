#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:47:12 2019

@author: toddbilsborough

Translates a route cipher control message as proof of concept
for decryption algorithm
"""

def main():
    """Translate a pre-generated route cipher encrypted message
    Output should be integers from ciphertext in order"""
    ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
    cipherlist = ciphertext.split(" ")
    rows = 5
    key = "-1 2 -3 4".split(" ")
    translation_matrix = []
    translation_string = ""
    for number in key:
        number = int(number)
        start = (abs(number) - 1) * rows
        end = start + rows
        row = cipherlist[start:end]
        if number > 0:
            row = row[::-1]
        translation_matrix.append(row)
    for _ in range(rows):
        for row in translation_matrix:
            translation_string += "{} ".format(str(row.pop()))
    print(translation_string)

if __name__ == '__main__':
    main()
