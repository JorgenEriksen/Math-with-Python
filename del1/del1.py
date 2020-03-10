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
sample = list(it.combinations(deck, 5))

suit  = lambda n : n % 4
value = lambda n : n % 13

def numVal(hand, number):
    placeholder = [0 for x in range(13)]
    for card in hand:
        placeholder[value(card)] +=1
        if(placeholder[value(card)] == number): return True
    return False

event = [x for x in sample if(numVal(x, 3) and numVal(x, 2))]


print("The probability is: ", len(event), "/", len(sample), "=", len(event)/len(sample))



#
# Task 4
#
# Calculate the probability (using list comprehension and itertools) 
# of drawing four jacks in a hand of five cards from a normal playing deck of 52 cards.

deck = list(range(52))
sample = list(it.combinations(deck, 5))

suit  = lambda n : n % 4
value = lambda n : n % 13

def numJacks(hand):
    return len([x for x in hand if value(x) == 11])
        
event = [x for x in sample if numJacks(x) >= 4]

print("The probability is: ", len(event), "/", len(sample), "=", len(event)/len(sample))



