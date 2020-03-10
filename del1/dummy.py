# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:08:22 2020

@author: Jørgen
"""

import itertools as it

#
# Task 5
#
# Ten people numbered 1,2,..10 are placed randomly in a queue.
# Calculate the probability (using list comprehension and itertools) of 
# person 1 being next to person 10 (directly infront of or directly behind) in the queue



people = list(range(10))
sample = list(it.permutations(people, 10))

event = [x for x in sample]

print("The probability is: ", len(event), "/", len(sample), "=", len(event)/len(sample))
