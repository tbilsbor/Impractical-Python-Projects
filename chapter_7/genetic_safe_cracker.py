#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:30:17 2019

@author: toddbilsborough

Project #14 from Impractical Python Projects

Objective
- Use a genetic algorithm to quickly find a safe's combination in 
a large search space

Notes
- Having copied the super rats mostly from the book, I'm going to try 
to do more of this one myself
- The safe takes a 10-digit code
- The book describes a hill-climbing algorithm which starts with an
arbitrary solution and changes a single number, keeping that part
of the solution whenever it works
- This simulates a sound detection approach to safe cracking, so the fitness
function doesn't indicate which indices have matched, just the number of
matches
- Results - Number of attempts is highly variant but the program always
runs very quickly

"""

import time
from random import randint

COMBINATION = '6822858902'

def fitness(combo, attempt):
    """Count the number of matches between the combination and the attempt"""
    grade = 0
    for c, a in zip(combo, attempt):
        if c == a:
            grade += 1
    return grade

def main():
    combo = [int(i) for i in COMBINATION]
    last_attempt = [randint(0, 9) for d in range(0, 10)]
    last_attempt_fitness = fitness(combo, last_attempt)
    attempts = 0
    while last_attempt != combo:
        next_attempt = last_attempt.copy()
        shift = randint(0, 9) # digit to change
        next_attempt[shift] = randint(0, 9)
        next_attempt_fitness = fitness(combo, next_attempt)
        if next_attempt_fitness > last_attempt_fitness:
            last_attempt = next_attempt.copy()
            last_attempt_fitness = next_attempt_fitness
        print(next_attempt, last_attempt)
        attempts += 1
    
    print("\nCombination found: {}".format(last_attempt))
    print("Attempts: {}".format(attempts))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("Found in {} seconds".format(end_time - start_time))
