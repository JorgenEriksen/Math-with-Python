




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


def suit(card):
    return card % 4 

