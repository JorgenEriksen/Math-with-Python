# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:08:22 2020

@author: Jørgen
"""
import random as rnd

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