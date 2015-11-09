# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:23:52 2015

@author: Goutham
"""
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import sklearn.metrics as metrics
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import PCA
#from sklearn.preprocessing import StandardScaler

def classification_report(clf,x_train, y_train):

    clf.fit(x_train, y_train)
    #let us use the trained classifier to predict the test set
    y_pred = clf.predict(x_test)

    # how good is our classifier
    print("The accuracy score is given by: ")
    print(metrics.accuracy_score(y_test, y_pred))

    print("Given below is the classification report: ")
    print(metrics.classification_report(y_test, y_pred, target_names=['bad', 'good']))

    #confusion matrix
    print("And, the confusion matrix is: ")
    print(metrics.confusion_matrix(y_test, y_pred))

os.chdir("C:/Users/Goutham/Downloads")
d = pd.read_csv("creditData_After_SMOTE_2.csv", quotechar= "'")

# Preprocessing of the data
# Using DictVectorizer
matrix = d.transpose().to_dict().values()
dv = DictVectorizer(sparse=False)
x = dv.fit_transform(matrix)
names = dv.get_feature_names()
data_frame = pd.DataFrame(x, columns = names)
data_frame.to_csv("creditData_After_DICT_VECTORIZER_3.csv")

# After removing the columns class=bad and class=good manually in Excel 
# Then manually add the Last Column as class from the previous step file
df = pd.read_csv("creditData_After_Class_Position_4.csv")

# Convert the data from bad / good to 0 and 1
df['class'] = df['class'].map({'bad': 0, 'good': 1})

# Using PCA of the top 25 features that are to be considered
pca_estimator = PCA(n_components=25)
train = pca_estimator.fit_transform(df)

# Extracting the Training and the Target Values
train = df.values
target = train[:,-1:]
train = train[:,:-1]

# Splitting the train data with 80/20 train and test split
x_train, x_test, y_train, y_test = train_test_split(train, target, \
test_size=0.40, random_state=33)
 
y_train=np.ravel(y_train)
y_test=np.ravel(y_test)

# Specify a classifier
 
     # LogisticRegression
clf_LogisticRegression = LogisticRegression(penalty='l2',                   \
dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1,     \
class_weight=None, random_state=33)
print("Given below is the classification report for LogisticRegression: ")
classification_report(clf_LogisticRegression,x_train, y_train)

    # SVM Linear
clf_SVM_Linear = SVC(kernel='linear', probability=True, random_state=33)
print("Given below is the classification report for SVM Linear: ")
classification_report(clf_SVM_Linear,x_train, y_train)

    # SVM RBF
clf_SVM_RBF = SVC(kernel='rbf', probability=True, random_state=33)
print("Given below is the classification report for SVM RBF: ")
classification_report(clf_SVM_RBF,x_train, y_train)

    # RandomForestClassifier
clf_RandomForestClassifier = RandomForestClassifier(n_estimators=10,        \
criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1,  \
max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False,  \
n_jobs=1, random_state=33, verbose=0)
print("Given below is the classification report for RandomForestClassifier: ")
classification_report(clf_RandomForestClassifier,x_train, y_train)

    # ExtraTreesClassifier 
clf_ExtraTreesClassifier = ExtraTreesClassifier(n_estimators=10,            \
criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1,  \
max_features='auto', max_leaf_nodes=None, bootstrap=False, oob_score=False, \
n_jobs=1,random_state=33, verbose=0)
print("Given below is the classification report for ExtraTreesClassifier: ")
classification_report(clf_ExtraTreesClassifier,x_train, y_train)
