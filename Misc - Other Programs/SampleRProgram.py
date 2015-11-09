# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:28:36 2015

@author: manghnani
"""

# Sample Code in R
from rpy2.robjects import r

r('install.packages("arules")')
r('library(arules)')
r('setwd("C:/Users/manghnani/Documents/R/Assignment-2")')
r('data <- read.transactions("basket.csv", format="basket", sep= ",")')
r('rules<-apriori(data, parameter = list(supp = 0.2, conf = 0.8))')
r('inspect(rules)')