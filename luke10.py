#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:34:46 2016

@author: MacBookPro
"""

eventyrer = {"tyv": 1, "trollmann": 1, "kriger": 1, "prest": 1}
survived = 0
fanger = 17

for rom in range(1, 101):
    goblins = rom
    lazarus = 0
    
    while True:
        # 1
        if eventyrer["tyv"] == 1 and goblins > 0:
            goblins -= 1
        
        # 2
        if eventyrer["trollmann"] == 1 and goblins > 0:
            if goblins > 10:
                goblins -= 10
            else:
                goblins = 0
        
        # 3
        if eventyrer["kriger"] == 1 and goblins > 0:
            goblins -= 1
        
        # 4
        if eventyrer["prest"] == 1 and lazarus == 0:
            if eventyrer["kriger"] == 0:
                eventyrer["kriger"] = 1
                lazarus += 1
            elif eventyrer["trollmann"] == 0:
                eventyrer["trollmann"] = 1
                lazarus += 1

        # 5
        if eventyrer["prest"]<= 0 and eventyrer["kriger"]<= 0 and eventyrer["trollmann"] <= 0:
            survived += goblins
            break
        
        # 6
        if goblins > 0:
            lever = 0
            for person in eventyrer:
                if eventyrer[person] == 1:
                    lever += 1
            if (goblins >= lever*10):
                if eventyrer["kriger"] == 1:
                    eventyrer["kriger"] = 0
                elif eventyrer["trollmann"] == 1:
                    eventyrer["trollmann"] = 0
                elif eventyrer["prest"] == 1:
                    eventyrer["prest"] = 0

        # 7
        if goblins <= 0:
            if eventyrer["kriger"] == 0:
                eventyrer["kriger"] = -1
            if eventyrer["trollmann"] == 0:
                eventyrer["trollmann"] = -1
            if eventyrer["prest"] == 0:
                eventyrer["prest"] = -1
            break
        
for surviver in eventyrer:
    if eventyrer[surviver] == 1:
        survived += 1
print "Overlevde: ",survived+fanger