#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:47:39 2019

@author: toddbilsborough

Impractical Python Projects #13 - Breeding an Army of Super-Rats

Objective
- Use a genetic algorithm to simulate breeding rats to an average
weight of 110 pounds

Notes
- All constants provided by the book; I might tweak them after I write
the program to see what happens
- The book deliberately does not take rat lifespan into account because
it's expected that rats will be culled by weight before they die of old age
- The book uses the statistics module; I'm going to try this with numpy
since I'm planning on working more with that in the future
- The book assumes an equal number of males and females and that all 
the females weigh less than all the males. Kind of weak, but I'll need
to wait to fix it until I get my head around this one.
- I'm ignoring the book's use of the time module. I can use timeit if I
want to see how fast the algorithm runs

Results
- Based on constants from the book, it takes 365 generations over 36 years
to get to the desired weight
- With more rats and a higher mutation rate, it takes 146 generations over
14 years
- 120 generations and 12 years for a higher litter size

"""

import random
import numpy as np

# CONSTANTS (all weights in grams)
GOAL = 50000 # Target weight in grams
NUM_RATS = 50 # Total number of rats the lab can support - must be even!
INITIAL_MIN_WT = 200 # Min weight of adult rat, in grams, in initial pop
INITIAL_MAX_WT = 600 # Max weight of adult rat, in grams, in initial pop
INITIAL_MODE_WT = 300 # Most common adult rat weight, in grams, in initial pop
MUTATE_ODDS = 0.05 # Probability of a mutation occuring in a rat
MUTATE_MIN = 0.5 # Scalar on rat weight of least beneficial mutation
MUTATE_MAX = 1.2 # Scalar on rat weight of most beneficial mutation
LITTER_SIZE = 12 # Number of pups per pair of mating rats
LITTERS_PER_YEAR = 10 # Number of litters per year per pair of mating rats
GENERATION_LIMIT = 500 # Generational cutoff to stop breeding program
        
def populate(num_rats, min_wt, max_wt, mode_wt):
    """Initialize a population with a triangular distribution of weights"""
    """Copied from the book"""
    return [int(random.triangular(min_wt, max_wt, mode_wt)) 
            for i in range(num_rats)]
    
def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target"""
    ave = np.mean(population)
    return ave / goal

def select(population, to_retain):
    """Cull a population to retain only a specified number of members"""
    """Copied from book"""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain // 2
    members_per_sex = len(sorted_population) // 2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females

def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population"""
    """Copied from book"""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds and fractional changes"""
    """Copied from book"""
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat * 
                                    random.uniform(mutate_min, mutate_max))
    return children

def main():
    """Create initial population, select, breed, mutate, display results"""
    """Largely copied from book"""
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, 
                       INITIAL_MODE_WT)
    print("Initial population weights = {}".format(parents))
    popl_fitness = fitness(parents, GOAL)
    print("Initial population fitness = {}".format(popl_fitness))
    print("Number to retain = {}".format(NUM_RATS))
    
    ave_wt = []
    
    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males, selected_females, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_males + selected_females + children
        popl_fitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, 
                                                      popl_fitness))
        ave_wt.append(int(np.mean(parents)))
        generations += 1
        
    print("Average weight per generation = {}".format(ave_wt))
    print("\nNumber of generations = {}".format(generations))
    print("Number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == "__main__":
    main()
