# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:30:48 2020

@author: Jørgen
"""

#
# map
#

a = [1, 2, 3, 4, 5]
b = 20
myadd2 = lambda x: x+2
b = list(map(myadd2, a)) # må ha med list pga promise
# b = [3, 4, 5, 6, 7]
print(b)
# a er uforantret

#
# filter
#

# returnerer true om x er mindre enn 6
lessthan6 = lambda x: x <6
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(filter(lessthan6, a))
# b = [1, 2, 3, 4, 5]
print (b)


#
# reduce
#

from functools import reduce

myadd = lambda x,y : x+y

a = [1, 2, 3, 4, 5]
val = reduce(myadd, a)
print(val)

#
# zip
#

a = [2, 3, 4, 5, 6]
b = [10, 20, 30]

c = list(zip(a, b))

print(c) # [(2, 10), (3, 20), (4, 30)]