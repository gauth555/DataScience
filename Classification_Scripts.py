# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:03:31 2018

@author: i58480
"""
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from sklearn import metrics as metrics
from sklearn.svm import SCV
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler


d = load_iris()
train = d.data
target = d.target

X_train, X_test, y_train, y_test = train_test_split(train,target,test_size = 0.2, random_state = 33)

#clf = SGDClassifier(loss = 'log')
clf = SCV(kernel = 'linear', probability = 'true', random_state = 33 )


# Let Us standardize the Features
ScalerX = StandardScaler()
X_train = ScalerX.fit_transform(X_train)
X_test = ScalerX.fit_transform(X_test)

#Specify the classifier
clf.fit(X_train, y_train)
#lets use the trained classifier to predict the test set
y_pred = clf.predict(X_test)
print (y_pred)
# To determine the probaility scores from the chosen classification model
y_prob = clf.predict_proba(X_test)
print (y_prob)

# To determine the Accuracy score from the chosen classification model
print ('The Accuracy score from the model is :')
print (metrics.accuracy_score(y_pred,y_test))

# To determine the Classification Report from the chosen classification model
print ('The classification report from the model is :')
print (metrics.classification_report(y_pred,y_test,target_names=['Sentosa','Versicolor','Virginica']))

# To determine the Confusion Matrix from the chosen classification model
print ('The Confusion Matrix from the model is :')
print (metrics.confusion_matrix(y_pred,y_test))