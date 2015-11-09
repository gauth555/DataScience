# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 06:57:26 2015

@author: manghnani
"""
"""
import random
number=random.randint(1,10)
guess_number=input('Guess a number between 1 and 10 or press q to quit : ')
while(guess_number!= 'q'):
    if guess_number==number:
        print('Yeah! you have got it right!')
        break
    else:
        print('Sorry! Please try again.')
        break
"""


import random
number2=random.randint(1,10)
while True:
    number=input("Enter a number between 1 and 10 or press q to quit : ")
    if number=='q':
        break
    elif number2<int(number):
        print('The number you entered was :' +str(number))
        print('\nThe number to be guessed was :' +str(number2))        
        print('\nThe number you entered was smaller than the number to be guessed')
        print('\nSorry! Please try again. Please try again or press q to quit')        
        continue        
        # break # Incase continue is given it goes into an infinite loop
    elif number2>int(number):
        print('The number you entered was :' +str(number))
        print('\nThe number to be guessed was :' +str(number2))        
        print('\nThe number you entered was larger than the number to be guessed')
        print('\nSorry! Please try again. Please try again or press q to quit')        
        continue        
        # break # Incase continue is given it goes into an infinite loop
    else:
        print("Congrats! Yes you have got it right in the first attempt")
        break