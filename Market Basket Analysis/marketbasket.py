# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 21:25:25 2015

@author: manghnani
"""
#Importing the packages
import pandas as pd
import os
# Changing the directory
os.chdir("C:\\Users\\manghnani\\Documents\\Python Scripts")
# Reading the CSV file
data=pd.read_csv("marketbasket.csv")
# Initializing the variables
matrix=0
names=0
matrix=data.values #Stores the values in the variable matrix
names= data.columns.values #Stores the column name values in the variable names
my_file = open("converted_market_basket.csv","w")
for row in range(matrix.shape[0]):# You should go through every row starting from row 0
    element="" # Initialize the variable element everytime a new row is read
    for col in range(1,matrix.shape[1]):
        if matrix[row][col].strip() =='true': # Checks if value is True
            element+=names[col]+"," # Append all the column names which have value True
    my_file.write(element[:-1] + "\n") # Write the record into the file
my_file.close() # Close the opened file after the loop ends


# Code to call execute the program in R console
# Importing the package r in python
from rpy2.robjects import r
r('install.packages("arules")') # Installing the packages for apriori rules
r('library(arules)') # Installing the library
r('setwd("C:/Users/manghnani/Documents/Python Scripts")') # Set the working directory
r('data <- read.transactions("converted_market_basket.csv", format="basket", sep = ",")')
r('rules<-apriori(data,parameter=list(supp=0.05,conf=0.50))')
r('rules')
r('inspect(rules)')
r('write(rules, file = "data.csv", quote=TRUE, sep = ",", col.names = NA)')
r('inspect(head(sort(rules,by="lift",decreasing=TRUE),5))')
r('pdf("itemFreq2.pdf")')
r('itemFrequencyPlot(data,support=0.05,horiz=TRUE,type=("relative"))')
r('dev.off()')
