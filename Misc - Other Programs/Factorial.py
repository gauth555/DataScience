# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 05:16:39 2015

@author: manghnani
"""

# Program to find the factorial of a number
def funct(n):
    result=1
    if n==0 or n==1:
        return result
    else:
        while n>1:
            result=result*n
            n=n-1
        return result
print(funct(5))