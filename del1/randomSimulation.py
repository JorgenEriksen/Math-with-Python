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

random = lambda n : n+rnd.randint(1,6)

for i in range(numSim):
    sum = 0
    for x in range(10): sum = random(sum)
    if sum == 30:
        hits += 1
    
print("the probability is ", hits / numSim)
#the probability is  0.048262

#
# task 2
#
# 10 people, numbered 1,2,..10, are placed randomly in a queue. 
# Calculate the probability that person 1 is located in some position 
# before person 10 (they do not need to be next to each other).


numSim = 500000
hits = 0
people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(numSim):
    rnd.shuffle(people)
    if people[0] < people[9]:
        hits += 1

print("the probability is ", hits / numSim)

#
# task 3
#
#

    