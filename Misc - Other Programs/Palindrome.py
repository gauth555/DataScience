# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 04:35:38 2015

@author: manghnani
"""
# This program is used to check for palindrome
def palindrome(name): # Defining the function palindrome having the parameter called name
    x=list(name) # Splitting the name into a list
    y=len(x) # Length of the name
    z=''#  Declaring the string variable z
    palindrome='' #  Declaring the string variable palindrome
    while(y>0): 
        z=x.pop() # Popping the last element
        palindrome=palindrome.extend(z) # Extending the element to the Palindrome
        y-=1 # Decrementing the counter
    palindrome=''.join(palindrome) # Joining the characters into string
    if name==palindrome: # Checking for if the reverse is the same
        print('The name you entered is a palindrome')
    else:
        print('The name you entered is not a palindrome')
# Calling the function Palindrome by passing the arguments to it
palindrome('Malayalam')
palindrome('Madam')
palindrome('Goutham')        