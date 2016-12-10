#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:33:51 2016

@author: MacBookPro
"""

position = [0,0]
val = 0
skattekart = open('skattekart.txt', 'r')

for line in skattekart:
    for word in line.split():
        if (word == 'walk') or (word == 'meters'):
            continue
        elif word == 'east':
                position[1] -= val
        elif word == 'west':
                position[1] += val
        elif word == 'north':
                position[0] += val
        elif word == 'south':
                position[0] -= val
        else:
            val = int(word)

print position
            