# -*- coding: utf-8 -*-

"""
Created on Mon Apr 13 14:11:05 2015

@author: Goutham
"""

# Homework 4 - Represents the credit worthiness of the customer
import os
import pandas as pd
import numpy as np
import sklearn.metrics as metrics
from sklearn.cross_validation import train_test_split
#from sklearn.feature_extraction import DictVectorizer
#from sklearn.decomposition import PCA
from sklearn.svm import SVC

os.chdir("C:/Users/Goutham/Downloads")
d = pd.read_csv("creditData_After_SMOTE_2.csv", quotechar= "'")

# Converting Attribute values into Numeric values

d['checking_status'] = d['checking_status'].map({'no checking': 0, '<0': 1, \
'0<=X<200': 2, '>=200': 3})

d['credit_history'] = d['credit_history'].map({'no credits/all paid': 0, \
'existing paid': 1, 'delayed previously': 2, \
'critical/other existing credit': 3, 'all paid': 4})

d['purpose'] = d['purpose'].map({'business': 0, 'domestic appliance': 1, \
'education': 2, 'furniture/equipment': 3, 'new car': 4, 'other': 5, \
'radio/tv': 6, 'repairs': 7, 'retraining': 8, 'used car': 9})

d['savings_status'] = d['savings_status'].map({'no known savings': 0, \
'<100': 1, '100<=X<500': 2, '500<=X<1000': 3, '>=1000': 4})

d['employment'] = d['employment'].map({'unemployed': 0, '<1': 1, \
'1<=X<4': 2, '4<=X<7': 3, '>=7': 4})

d['personal_status'] = d['personal_status'].map({'male single': 0, \
'male mar/wid': 1, 'male div/sep': 2, 'female div/dep/mar': 3})

d['other_parties'] = d['other_parties'].map({'none': 0, \
'guarantor': 1, 'co applicant': 2})

d['property_magnitude'] = d['property_magnitude'].map({'car': 0, \
'life insurance': 1, 'no known property': 2, 'real estate':3})

d['other_payment_plans'] = d['other_payment_plans'].map({'bank': 0, \
'none': 1, 'stores': 2})

d['housing'] = d['housing'].map({'for free': 0, 'own': 1, 'rent': 2})

d['job'] = d['job'].map({'high qualif/self emp/mgmt': 0, 'skilled': 1, \
'unemp/unskilled non res': 2, 'unskilled resident': 3})

d['own_telephone'] = d['own_telephone'].map({'none': 0, 'yes': 1})

d['foreign_worker'] = d['foreign_worker'].map({'no': 0, 'yes': 1})

d['class'] = d['class'].map({'bad': 0, 'good': 1})

# Extracting the Training and the Target Values
train = d.values
target = train[:,-1:]
train = train[:,:-1]

#let us split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(train, target, \
 test_size=0.41, random_state=33)
 
y_train=np.ravel(y_train)
y_test=np.ravel(y_test)
 
#specify a classifier
    # SVM RBF
clf = SVC(kernel='rbf', probability=True, random_state=33)
print("Given below is the classification report for SVM RBF: ")
clf.fit(x_train, y_train)

#let us use the trained classifier to predict the test set
y_pred = clf.predict(x_test)

#how good is our classifier
print("The accuracy score for the SVM RBF is: ")
print(metrics.accuracy_score(y_test, y_pred))

print("Given below is the classification report for the SVM RBF: ")
print(metrics.classification_report(y_test, y_pred, target_names=['bad', 'good']))

#confusion matrix
print("And, the confusion matrix is: ")
print(metrics.confusion_matrix(y_test, y_pred))