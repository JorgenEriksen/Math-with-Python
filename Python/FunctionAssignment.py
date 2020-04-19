# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:43:45 2020

@author: Jørgen
"""

# A)
# Create a list of square numbers less than one million which have remainder 3 when
# divided by 4, by performing the following operations.

# 1. Create a list [0, 1, 2, ..., 1000000] using ”range”
num = [x for x in range(1000000)]

# 2. Use the list from 1. and the function ”map” to create a list of squares.
makeSquare = lambda x: x*x
num = list(map(makeSquare, num))

# 3. Use the result from 2. and the function ”filter” to compute the answer.
lessThanMill = lambda x: x<1000000
threeInReminder = lambda x: x%4 == 3 

num = list(filter(lessThanMill, num))
num = list(filter(threeInReminder, num))


# B)
# Solve the ”Opening and closing doors” puzzle with 1024 doors using map and filter
# (you may need zip). An example was given in the lectures using list comprehension,
# so all you have to do is translate the code
lessThan1025 = lambda x: x<1025
num = [x for x in range(100)]
num = list(map(makeSquare, num))
num = list(filter(lessThan1025, num))

if(num[-1] == 1024):
    print("The door is open")
else:
    print("The door is closed")


# C)



# D)
# In this problem you will use map and lambdas to work on lists of list
    
# Implement a function ”envelop”, which takes a list of numbers as input and
# produces a lists of lists of one element. I.e.
# envelop [13,4,1] = [[13],[4],[1]]

envelop = lambda x: [[y] for y in x]
number =  [13, 4, 1]
print(envelop(number))

# Implement a function ”last”, which takes a list of lists as input, and produces
# the list of the last element in each list. I.e.
# [[1,2,3],[4],[5,6,7]] = [3,4,7]
last = lambda x: [y[-1] for y in x]
number = [[1,2,3],[4],[5,6,7]]
print(last(number))


# Implement a function ”length”, which takes a list of lists as input, and produces
# the list of lengths of these lists. I.e.
# [[1,2,3],[],[4,3,2,1],[1]] = [3,0,4,1]

number =  [[1,2,3],[],[4,3,2,1],[1]]
length = lambda x: [len(y) for y in x]
print(length(number))


# E)
# If you run the code
# l = list(map(print, ["Hope","You","Are", "Well!"]))
# s = list(map(print, "Hope You Are Well!"))
#you may or may not be surprised at the result. In either case, figure out what is
# going on and explain.

l = list(map(print, ["Hope","You","Are", "Well!"]))
s = list(map(print, "Hope You Are Well!"))

# my answer: 
# l[0] is "hope" as the list is split up in 4 elements.
# s does not have [] so that means that each character is a element in list.
# So s[0] is 'H', s[1] is 'o' and so on.



# F)
# Use reduce to implement the function product which computes the product of a list
# of integers. I.e.
# [1,2,3,4,5] = 1*2*3*4*5
from functools import reduce

number = [1, 2, 3, 4, 5]

multTogether = lambda x: reduce((lambda y, z: y*z), x)
print(multTogether(number))


# G)
# Without using loops, using only map, filter, zip, and lambdas, and in one line
# of code, implement the function ”take” which takes the first n elements from a list.
# E.g.
# take(4, [1,2,3,4,50,60,70,80]) = [1,2,3,4]

# take = lambda y, x: [z for z in x[:y]]

take = lambda y, x: list(filter(lambda z: z<=y, x))
print(take(4, [1,2,3,4,50,60,70,80]))






