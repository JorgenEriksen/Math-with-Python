# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:08:22 2020

@author: Jørgen
"""

doors = [False for i in range(1024)]
for i in range(1024):
    for j in range(i, 1024, i + 1):
        doors[j] = not doors[j]
doors = [i + 1 for i in range(1024) if doors[i]]
print(doors)