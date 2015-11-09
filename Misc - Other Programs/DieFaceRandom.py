# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 05:23:40 2015

@author: manghnani
"""

# This is a rolling die program to roll the die 1000 times and count the
# the number of times the number appears on the die

import random
counters={}
count=0
while count<1000:
    die_number=random.randint(1,6)
    if die_number in counters:
        counters[die_number]=counters[die_number]+1
    else:
        counters[die_number]=1
    count=count+1
    counters.items()  