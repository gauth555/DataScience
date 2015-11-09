# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:35:32 2015

@author: Goutham
"""
# Using Linear regression() (from sklearn.linear_model) with stanardization 
# and KFold
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

d = load_boston()
print (len(d))
print (d.values())

train = d.data
target = d.target

#use scaler
scalerX=StandardScaler()
scalerY=StandardScaler()
target=scalerY.fit_transform(target)


clf=LinearRegression(fit_intercept=True)
cv=KFold(len(train),10,shuffle=True,random_state=33)
score=cross_val_score(clf,train,target,cv=cv)
print("Score:{}".format(score.mean()))