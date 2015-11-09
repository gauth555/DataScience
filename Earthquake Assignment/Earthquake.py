# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 20:17:45 2015

@author: manghnani
"""
# Earthquake Data
import pandas as pd

import os
from collections import Counter
os.chdir("C:\\Users\\manghnani\\Documents\\Python Scripts\\Earthquake Assignment")
df=pd.read_csv("data.csv")



#df=pd.read_csv("F:\!DATA SCIENCE - Python\Datasets\data.csv")

y=list(df['place'])
c= Counter(y)
print (c.most_common(5))

#names=df.values
#print names)

#print(df.describe)
#pandas.DataFrame.min

#df['Gender']=df['Gender'].map({"Male":"Gender", "Female":"" })
# print(df)
