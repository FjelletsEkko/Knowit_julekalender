#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:17:10 2016

@author: MacBookPro
"""

transactions = open("luke9_file.txt", "r")
accounts = {}
for line in transactions:
    i = 1
    for entry in line.split(","):
        if i == 1:
            acc_from = entry
        elif i == 2:
            acc_to = entry
        else:
            money = entry
        i += 1
        
    if not acc_from in accounts:
        accounts[acc_from] = -int(money)
    else:
        accounts[acc_from] -= int(money)

    if not acc_to in accounts:
        accounts[acc_to] = int(money)
    else:
        accounts[acc_to] += int(money)
        
num = 0
for account in accounts:
    if accounts[account] > 10:
        num += 1
print num
        
        