# -*- coding: utf-8 -*-

"""
Created on Mon Feb  9 10:10:46 2015

@author: manghnani
"""

# Assignment 2
# Importing the packages
import os
import math
# Prompting the User to enter the directory
dir=input("Enter Dir:")
os.chdir(dir)
# Reading the file reviews.txt and then saving the contents into a variable
my_file=open("reviews.txt","r")
# reviews_dict is a dictionary using the eval function
reviews_dict=eval(my_file.read())

# Computing the similarity between two reviewers
def getSimilarity(a,b):
    movie_review1=reviews_dict.get(a) #Getting the value for the key 'a' specified
    movie_review2=reviews_dict.get(b) #Getting the value for the key 'b' specified
# Initializing the variables sum1 and score to 0
    sum1=0
    score=0
# Checking for the common movies viewed by both reviewers
# And find the Euclidian distance
    for k in movie_review1:
        if k in movie_review2:
            v1=movie_review1[k]
            v2=movie_review2[k]
            sum1 += math.pow((v1-v2),2)
        score=math.sqrt(sum1)
    return score
# Passing the arguments to the function getSimilarity and storing it in Score
score=getSimilarity("Peter", "Trevor Chappell")
print(score)

# The second method to get the similarity between all the two reviewers
def getSimilarities(a):
# Extracting all the reviewers from the dictionary
    reviewers={key for key, val in reviews_dict.items()}
# Reading all the values of the reviewers from the dictionary    
    for b in reviewers:
        if b==a: # If the argument passed is the same as the value read
            continue # Just continue loop and ignore the remaining loop
        else: # Else print the other reviewers with the Euclidian distance
            print(a,b, "\t", "%.2f" %getSimilarity(a,b))
getSimilarities("Peter")