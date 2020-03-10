# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:46:16 2020

@author: Jørgen
"""
import itertools as it

# Task 1
#
# Calculate the probability (using list comprehension and itertools) of 
# rolling at least 4 sixes when you roll 7 fair dice with values 1,2,3,4,5,6.
#

dice = [1, 2, 3, 4, 5, 6]
sample = list(it.product(dice, repeat = 7))

def numOfSixes(number):
    return len([j for j in number if j == 6])

event = [i for i in sample if numOfSixes(i) >= 4]

#The probability is:  4936 / 279936 = 0.01763260173754001
print("The probability is: ", len(event), "/", len(sample), "=", \
      len(event)/len(sample))


# Task 2
#
# Calculate the probability (using list comprehension and itertools) of 
# rolling a sum equal to 35 when you roll 7 fair dice with values 1,2,3,4,5,6.
#

dice = [1, 2, 3, 4, 5, 6]
sample = list(it.product(dice, repeat = 7))

def sumValue(number):
    sum = 0
    for j in number:
        sum += j
    return sum
        
event = [i for i in sample if sumValue(i) == 35]


# The probability is:  1667 / 279936 = 0.005954932556012803
print("The probability is: ", len(event), "/", len(sample), "=", \
      len(event)/len(sample))


# Task 3
#
# Calculate the probability (using list comprehension and itertools) of 
# drawing a full house from a normal playing deck of 52 cards.
#

deck = list(range(52))
sample = list(it.combinations(deck, 4))

suit  = lambda n : n % 4
value = lambda n : n % 13

event = 0;

def checkPair(hand, cardNum, avoidCard):
    return len([card for card in hand if value(card) == cardNum and value(card) != avoidCard])

def checkThree(hand, cardNum):
    return len([card for card in hand if value(card) == cardNum])

def event():
    sum = 0
    for x in range(13):
        three = [hand for hand in sample if checkThree(hand, x) == 4]       
        for y in range(13):
            two = [hand for hand in three if checkPair(hand, y, x) == 2]
        sum += len(two)
    return sum

event += event()

print("The probability is: ", event, "/", len(sample), "=")


