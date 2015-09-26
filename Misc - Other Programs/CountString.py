# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 08:48:55 2015

@author: manghnani
"""
# This program is used to count the number of words in a string
def count(sample): # defining the function count having the parameter 'sample'
    y=0            # initializing the variabe y to 0 
    x=sample.split() # Splitting the string into a list of words
    y=len(x) # Getting to know the length of the list x
    print('The number of words in the string is : %s'%y)
#Calling the function count by passing the argument as the string
count("Welcome to the python course")
count("Goutham chandru Manghnani")
