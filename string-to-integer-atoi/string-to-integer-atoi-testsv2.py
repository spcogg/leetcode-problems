# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:46:39 2019

@author: Hungy
"""

#def myAtoi(self, x: str) -> int:
x = ' -313'
if x == '':  # handle empty case
    print(0)
#        return 0
a = x.lstrip()  # strip left spaces
# add char to a new str, continue until non-numeric reached
b = ''
neg = False
for i in range(len(a)):  # check every char
    if a[i].isnumeric():  # only add numerics
        b += a[i]
        print(b)
    elif i == 0:  # unless it's the first char, then check if negative
        # this was really dumb - forgot to handle + - case, and . decimals slipping past
        if a[i] == '-':
            neg = True  # remember & handle later
    else:
        break
print(b)
if len(b) == 0 or b == '-':
    print(0)
	#return 0  # handle null cases
if neg:
    print(-int(b))
	#return -int(b)  # else convert to int and return
else:
    print(int(b))




