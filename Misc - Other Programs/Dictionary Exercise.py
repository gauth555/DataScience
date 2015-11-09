# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 23:06:47 2015

@author: manghnani
"""
# Assignment 1
# Prompting the User to enter the directory
import os
dir=input("Enter Dir:")
os.chdir(dir)
# Reading the file words.txt and then saving the contents into my_file variable
my_file=open("words.txt","r")
#Creating a dictionary and then moving the contents from the file into the dict
dictionary1={}
for line in my_file:
    x=line.split(":")
    a=x[0]
    b=x[1]
    c=len(b)-1 # The -1 gets the lenght of b minus'\n'
    b=b[0:c] # from element zero upto but not including the \
    dictionary1[a]=b
