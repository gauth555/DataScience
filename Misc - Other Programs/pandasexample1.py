# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:22:34 2015

@author: manghnani
"""
import os
dir=input("Enter Dir:")
os.chdir(dir)
# Reading the file words.txt and then saving the contents into my_file variable
my_file=open("words.txt","r")

import pandas as pd
f = open("reviews.txt")
d=eval(f.read())
print(d)
df=pd.DataFrame(d)
#print(df[['Peter','Trevor Chappell']].dropna().corr())
#print(df.corr())
#print(df.describe())
# dROP na IS REMOVING ALL THE THE NOT APPLICABLE rows
# corr is a function for co relations

# to will it up with zeros

print (df.fillna(0))
