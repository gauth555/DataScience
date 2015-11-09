# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 09:22:44 2015

@author: manghnani
"""

# Function to compute the nth Fibonacci numbers
def fibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-1)+ fibonacci(number-2)            
    
# Calling the function Fibonacci by passing the argument
print(fibonacci(5))
print(fibonacci(7))