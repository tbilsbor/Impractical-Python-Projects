#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:47:39 2019

@author: toddbilsborough

Impractical Python Projects Ch 7
Rat harem challenge project

Objective
- Use a genetic algorithm to simulate breeding rats to an average
weight of 110 pounds
- Accomodate a variable number of male and female individuals (since a
single male rat can mate with multiple females)

Notes
- I have a choice now as to whether to just breed the male rats to the
desired average weight or to try to get the entire population up to that
weight. The latter seems most in keeping with the spirit of the exercise.
- I'll also set it up so that the male rats are breeding freely with female
rats rather than being restricted to a certain number each, which seems more
realistic

Results
- After a few runs, it appears that the rat harem is much faster than having
equal populations

"""

import random
import numpy as np

# CONSTANTS (all weights in grams)
GOAL = 50000 # Target weight in grams
NUM_MALE_RATS = 4 # Total number of male rats
NUM_FEMALE_RATS = 16 # Total number of female rates. Male + fem must be even!
INITIAL_MIN_WT = 200 # Min weight of adult rat, in grams, in initial pop
INITIAL_MAX_WT = 600 # Max weight of adult rat, in grams, in initial pop
# Most common male adult rat weight, in grams, in initial pop
INITIAL_MODE_WT_MALE = 300
INITIAL_MODE_WT_FEMALE = 250
MUTATE_ODDS = 0.01 # Probability of a mutation occuring in a rat
MUTATE_MIN = 0.5 # Scalar on rat weight of least beneficial mutation
MUTATE_MAX = 1.2 # Scalar on rat weight of most beneficial mutation
LITTER_SIZE = 12 # Number of pups per pair of mating rats
LITTERS_PER_YEAR = 8 # Number of litters per year per pair of mating rats
GENERATION_LIMIT = 500 # Generational cutoff to stop breeding program

def populate_male(num_male_rats, min_wt, max_wt, mode_wt_male):
    """Initialize a population with a triangular distribution of weights"""
    initial_male_population = [
        int(random.triangular(min_wt, max_wt, mode_wt_male)) for
        i in range(num_male_rats)]
    return initial_male_population

def populate_female(num_female_rats, min_wt, max_wt, mode_wt_female):
    """Initialize a population with a triangular distribution of weights"""
    initial_female_population = [
        int(random.triangular(min_wt, max_wt, mode_wt_female)) for
        i in range(num_female_rats)]
    return initial_female_population

def fitness(population, goal):
    """Measure population fitness based on an attribute mean vs target"""
    ave = np.mean(population)
    return ave / goal

def select(population_male, population_female,
           to_retain_male, to_retain_female):
    """Cull a population to retain only a specified number of members"""
    females = sorted(population_female)
    males = sorted(population_male)
    selected_females = females[-to_retain_female:]
    selected_males = males[-to_retain_male:]
    return selected_males, selected_females

def breed(males, females, litter_size):
    """Crossover genes among members (weights) of a population"""
    children_male = []
    children_female = []
    for female in females:
        for child in range(litter_size):
            male = random.choice(males)
            if female <= male:
                child = random.randint(female, male)
            else:
                child = random.randint(male, female)
            if random.randint(0, 1) == 0:
                children_male.append(child)
            else:
                children_female.append(child)
    return children_male, children_female

def mutate(children_male, children_female,
           mutate_odds, mutate_min, mutate_max):
    """Randomly alter rat weights using input odds and fractional changes"""
    for index, rat in enumerate(children_male):
        if mutate_odds >= random.random():
            children_male[index] = round(rat *
                                         random.uniform(mutate_min,
                                                        mutate_max))
    for index, rat in enumerate(children_female):
        if mutate_odds >= random.random():
            children_female[index] = round(rat *
                                           random.uniform(mutate_min,
                                                          mutate_max))
    return children_male, children_female

def main():
    """Create initial population, select, breed, mutate, display results"""
    generations = 0
    parents_male = populate_male(NUM_MALE_RATS, INITIAL_MIN_WT,
                                 INITIAL_MAX_WT, INITIAL_MODE_WT_MALE)
    parents_female = populate_female(NUM_FEMALE_RATS, INITIAL_MIN_WT,
                                     INITIAL_MAX_WT, INITIAL_MODE_WT_FEMALE)
    print("Initial male population weights = {}".format(parents_male))
    print("Initial female population weights = {}".format(parents_female))
    popl_fitness = fitness(parents_male + parents_female, GOAL)
    print("Initial population fitness = {}".format(popl_fitness))
    print("Number of males to retain = {}".format(NUM_MALE_RATS))
    print("Number of females to retain = {}".format(NUM_FEMALE_RATS))

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents_male,
                                                  parents_female,
                                                  NUM_MALE_RATS,
                                                  NUM_FEMALE_RATS)
        children_male, children_female = breed(selected_males,
                                               selected_females,
                                               LITTER_SIZE)
        children_male, children_female = mutate(children_male,
                                                children_female,
                                                MUTATE_ODDS,
                                                MUTATE_MIN,
                                                MUTATE_MAX)
        parents_male = selected_males + children_male
        parents_female = selected_females + children_female
        popl_fitness = fitness(parents_male + parents_female, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations,
                                                      popl_fitness))
        ave_wt.append(int(np.mean(parents_male + parents_female)))
        generations += 1

    print("Average weight per generation = {}".format(ave_wt))
    print("\nNumber of generations = {}".format(generations))
    print("Number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == "__main__":
    main()
