# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:46:09 2020

@author: Jørgen
"""

#
# task 1
#
# Calculate the probability of having sum 30 when rolling 10 fair dice. 
# Experiment with the appropriate number of simulations (numSim)

import random as rnd

numSim = 500000
hits = 0
for i in range(numSim):
    sum = 0
    for x in range(10):
        randomNum = rnd.randint(1,6)
        sum += randomNum
    if sum == 30:
        hits += 1
    
print("the probability is ", hits / numSim)

#
# task 2
#
# 10 people, numbered 1,2,..10, are placed randomly in a queue. 
# Calculate the probability that person 1 is located in some position 
# before person 10 (they do not need to be next to each other).

import random as rnd

numSim = 500000
hits = 0
for i in range(numSim):
    
