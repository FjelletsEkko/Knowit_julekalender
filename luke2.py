#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:25:20 2016

@author: MacBookPro
"""

n, m, mysum = 1, 1, 0
while m<4000000000:
    if m % 2 == 0:
        mysum += m
    n, m = m, n + m
print mysum