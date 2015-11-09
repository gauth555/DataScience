# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 06:57:26 2015

@author: manghnani
"""

import random
number=random.randint(1,10)
guess_number=input('Guess a number between 1 and 10 ')
if guess_number<str(number):
    print('The number you entered was :' +guess_number)
    print('\nThe number to be guessed was :' +str(number))        
    print('\nThe number you entered was smaller than the number to be guessed')
    print('\nSorry! Please try again.')
elif guess_number>str(number):
    print('The number you entered was :' +guess_number)
    print('\nThe number to be guessed was :' +str(number))        
    print('\nThe number you entered was larger than the number to be guessed') 
else:
    print('Yeah! you have got it right!')