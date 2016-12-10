# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Undersøk om element er delbar med '7'
def delbar(num):
    if num%7 == 0:
        return True
    return False

# Undersøk om element inneholder '7'
def ink_7(num):
    s=str(num)
    found_7 = 0
    for j in range(len(s)):
        if s[j] == "7":
            found_7 = 1
    if found_7 == 1:
        return True
    return False

# Lag liste med alt som kan deles med 7 eller inneholder 7
def check_7(maks):
    special = []
    for i in range(1, maks):
        if delbar(i) or ink_7(i):
            special.append(i)
    return special


if __name__== "__main__":
    specials = check_7(1338)
    while True:
        i = 1
        new = []
        for special in specials:
            if delbar(special) or ink_7(special):
                new.append(i)
                i += 1
            else:
                new.append(special)
        if specials == new:
            print specials[-1]
            break
        specials = new