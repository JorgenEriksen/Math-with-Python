




mylist = [10,20,30,40,50,60,70,80,90]

import random as rnd
print(rnd.random())

#random, inkluderer begge tallene
print(rnd.randint(1, 2))

randomlist = [rnd.randint(0, 1) for i in range(100)]
print(randomlist)

mylist = [[1,2,3],[],[],[4,5]]
lenlist = [len(x) for x in mylist]
print(lenlist)
    
deck = [x for x in range(52)]

#def er funksjon, suit er funksjonnavnet, card er agumentet
def suit(card):
    return card % 4 

def value(card):
    return card % 13

print(suit(51), value(51));

#annen måte å lage funksjoner. lambda input : output
suit = lambda card : card % 4
value = lambda card : card % 13

print("#####")
print("#####")
print("#####")
      
      
import itertools as it
mylist = [1, 2, 3, 4, 5]
# 5C2 = 10. like mange som i listen under. Må ha med list.
comb = list(it.combinations(mylist, 2))
print(comb)

# alle mulige 5 kort hånd fra et deck
sample = list(it.combinations(deck, 5))
#52C5
print(len(sample))
print(sample[10])

def numAce(hand):
    return len([x for x in hand if value(x) == 0])

event = [hand for hand in sample if numAce(hand) > 0]

print("The probability of one or more aces is", len(event) , "/", \
      len(sample), "=", len(event)/len(sample))


print("*****")
print("*****")
print("*****")

from copy import copy, deepcopy
# array blir ikke kopiert med referert ved a = b.
# for å kopiere bruk  a = b.copy()
#deepcopy er det beste å bruke for mitt bruk

#
# list comprehension
#

#good
mylist = [2*i+1 for i in range(0,50)]
print(mylist)

# lagrer kun de som som kan deles med 3 fra mylist
mylist2 = [i for i in mylist if i % 3 == 0]
print(mylist2)


suit = lambda n : n % 4
value = lambda n : n % 13

suits = ["clubs", "hearts", "spades", "diamonds"]

print("farge til kort 34 er ",suits[suit(34)])

#
# itertools
#
# combinations er uten rekkefølge, product er med rekkefølge
import itertools as it

# sample space

deck = list(range(52))
sample = list(it.combinations(deck, 5))
# 52C5
print(len(sample))


#
# Levering
#
# 0 er ace

def numAces(hand):
    return len([card for card in hand if value(card) == 0])

# er helt lik som funksjonen over
numAces2 = lambda hand : len([card for card in hand if value(card) == 0])

event = [hand for hand in sample if numAces2(hand) > 0]

print("The probability is: ", len(event), "/", len(sample), "=", \
      len(event)/len(sample))


print("&&&&&")
print("&&&&&")
print("&&&&&")


#
# Dice
#


#dice = [i+1 for i in range(6)]
dice = [1, 2, 3, 4, 5, 6]
sample = list(it.product(dice, dice))
#sample = list(it.product(dice, repeat = 8)) er 8 terninger
print(sample)
