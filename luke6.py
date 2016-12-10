#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:19:37 2016

@author: MacBookPro
"""
x, y = 0, 0
koor = [x, y]

koor[0] += 4
print koor[0]
empty = []

plusplus = koor[0]+1 + koor[1]+1
plusmin = koor[0]+1 + koor[1]-1
minplus = koor[0]-1 + koor[1]+1
minmin = koor[0]-1 + koor[1]-1
new = max(plusplus, plusmin, minplus, minmin)
if minmin == new:
    empty.append(minmin)
if minplus == new:
    empty.append(minplus)
if plusmin == new:
    empty.append(plusmin)
if plusplus == new:
    empty.append(plusplus)
print empty