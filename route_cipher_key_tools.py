#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:54:23 2019

@author: toddbilsborough

From Storing a Key as a Dictionary project from chapter 4 of
Impractical Python Projects

Objective 1 - Write a short script to break a route cipher key into two parts:
one to record the column order and one to record the direction to read 
through the rows in the column (up or down). Store the column number
as a dictionary key and the reading direction as the dictionary value.
Have the program interactively request the key value for each column from
the user.

Objective 2 - Generate a collection of all possible keys for a given
number of columns
"""

from itertools import permutations
from itertools import product

def generate_direction_masks(cols):
    """Generates strings of binary numbers representing
    directions in which to read columns
    0 for down
    1 for up
    For example, cols=3 will generate the strings
    000, 001, 010, 011, 100, 101, 111"""
    return list(product('01', repeat=cols))

def generate_keys(cols):    
    """Generator: yields all possible keys for a given number of columns"""
    direction_masks = generate_direction_masks(cols)
    for seq in permutations(range(1, cols + 1)):
        for mask in direction_masks:
            key = []
            for number, direction in zip(seq, mask):
                if direction == '0':
                    key.append(number)
                elif direction == '1':
                    key.append(-number)
            yield key

def input_key(cols):
    """Prompts for user input of a route cipher key"""
    key = {}
    for col in range(cols):
        column_order = input("\nColumn to read: ")
        column_dir = ""
        while (column_dir != "up" and column_dir != "down"):
            column_dir = input("\nDirection (up or down): ").lower()
        key[column_order] = column_dir
    return key
