# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:51:29 2015

@author: manghnani
"""

import pandas as pd
import os
os.chdir("C:\\Users\\manghnani\\Documents\\Python Scripts")
df = pd.read_csv("genderage.txt")
#print(df)
#df['Gender']=df['Gender'].map({("Male","Mate"):0, "Female":1})# Change the file from mate to male
#print(df)

df['Gender']=df['Gender'].map({"Male":"Gender", "Female":"" })
print(df)

