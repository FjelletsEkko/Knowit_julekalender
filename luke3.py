#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:24:36 2016

@author: MacBookPro
"""

from collections import Counter

friends, enemies, sort_friend, sort_hater = [], [], [], []
knowit_file = open('knowit_luke3.txt', 'r')

# Separerer venne- og hatlista
for line in knowit_file:
    for word in line.split():
        if word == 'friends':
            friends.append(line)
        elif word == 'hates':
            enemies.append(line)
            
# Sorter ut kun vennenavn
for line in friends: 
    empty = []
    for word in line.split():
        if word == 'friends':
            continue
        else: 
            empty.append(word)
    sort_friend.append(empty)
    
    
konvertert_venn = []
redusert_venn = []

# Bytter rekkefølge for å senere teste om duplikat
for forhold in sort_friend:
    empty = []
    empty.append(forhold[1])
    empty.append(forhold[0])
    konvertert_venn.append(empty)

# Reduserer vennelista ved å kun ta med ikke-duplikat videre
for i in sort_friend:
    x = 0
    for j in konvertert_venn:
        if i == j:
            x = 1
    if x == 0:
        redusert_venn.append(i)

# Sorter ut kun haternavn
for line in enemies:
    empty = []
    for word in line.split():
        if word == 'hates':
            continue
        else:
            empty.append(word)
    sort_hater.append(empty)

konvertert_hat = []
redusert = []

# Bytter rekkefølge i hatforholdet for å teste senere
for forhold in sort_hater:
    empty = []
    empty.append(forhold[1])
    empty.append(forhold[0])
    konvertert_hat.append(empty)

# Tar kun med ikke-duplikater videre
for i in sort_hater:
    x = 0
    for j in konvertert_hat:
        if i == j:
            x = 1
    if x == 0:
        redusert.append(i)

# Finn hater som hater sin egen venn.
hatelista = []
for line in redusert:
    hater, hatet = line[0], line[1]
    for venn in redusert_venn:
        if (hater == venn[0] and hatet == venn[1] or (hater == venn[1] and hatet == venn[0])):
            hatelista.append(hater)

print Counter(hatelista)
knowit_file.close()