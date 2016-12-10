#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:53:21 2016

@author: MacBookPro
"""


number = 16
while number<1000000000:
    nytt = []
    number = str(number)
    nytt.append(number[-1])
    for i in range(len(number)-1):
        nytt.append(number[i])
    number = int(number)
    nytt = int(''.join(nytt))
    if nytt == 4*number:  
        print number
        break
    number += 10


"""new_num = number % 10
print new_num
difference = number - new_num
my_string = str(new_num)
number = str(number)
lengde = (len(number) - 1)


print my_string"""