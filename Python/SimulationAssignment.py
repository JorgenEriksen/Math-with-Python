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

random = lambda: rnd.randint(1,6)

hits = [i for i in range(numSim) if sum([random() for x in range(10)]) == 30]

print("the probability is ", len(hits) / numSim)
# the probability is  0.048574

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
    if people[0] < people[9]: hits += 1

print("the probability is ", hits / numSim)

# the probability is  0.500656

#
# task 3
#
# Two disks with radius 2 are located at the positions (0.0) and (2,0). Calculate the area of their intersection. (i.e. the area they have in common.)










#
# task 4
#
# Calculate the probability of rolling all sixes when you roll 20 fair dice with values 1,..,6.

import random as rnd

numSim = 1000000

random = lambda: rnd.randint(1,6)


hits = [x for x in range(numSim) if len([x for x in range(20) if random() == 6]) == 20]

print("the probability is ", len(hits)/numSim)


#
# task 5
#
# Write a simulation which shows that the best strategy in the Monty Hall Problem is to change door.

numSim = 100
doorChoosen = 2


def findLastDoor(num1, num2):
    if num1+num2 == 1: return 2
    elif num1+num2 == 2: return 1
    else: return 0

def randomTwoOtherDoors(num1):
    if num1 == 1: return rnd.randint(0, 2)
    elif num1 == 2: return rnd.randint(0, 1)
    else: return rnd.randint(1, 2)

def event(): 
    doors = [False, False, False]
    correctDoor = rnd.randint(0,2)
    doors[correctDoor] = True
    
    if (doorChoosen == correctDoor): doorRemoved = randomTwoOtherDoors(doorChoosen)
    else: doorRemoved = findLastDoor(doorChoosen, correctDoor)
    
    newDoor = findLastDoor(doorChoosen, doorRemoved)
    if doors[newDoor]: return True
    return False

hits = [x for x in range(numSim) if event() ]

print("the probability is ", len(hits) / numSim)
# the probability is  0.67
