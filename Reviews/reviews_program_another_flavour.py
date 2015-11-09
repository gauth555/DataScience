# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 19:06:46 2015

@author: manghnani
"""
import math #for calculating sqrt
def getsimilarity(name1,name2): #method 1 definition
    c1={} #empty dictionaries to store the dictionary inside the mai n dictionary
    c2={}
    c1=dict[name1] #store the review names and score for first reviewer
    c2=dict[name2] #store review names and score for second reviewer
    s1=set()#empty set
    s2=set()#empty set
    for i in c1: #adding values to set to comapare the common reviews
        s1.add(i)
    for i in c2:
        s2.add(i)
    s3=s1 & s2 #intersection - only those common to both reviewers appear
    ed=0
    for i in s3:
       
        ed=(c1[i]-c2[i])**2+ed #calculating the square of eu distance 
    
    ed=math.sqrt(ed)    #eu distance
    return ed

def getsimilarities(name1):
    
    c2=(dict.keys()) #extracting reviewer names
    s4=set() #empty sets
    s5=set()
    s4={name1} #the reviewer that should be compared against all the others
    for i in c2:
        s5.add(i)   
    s6=s5-s4 #list of all other reviewers
    for i in s6:
             print(name1,i, "\t", "%.2f" %getsimilarity(name1,i) )
    #calling a function1 inside function2 to calculate eu distance
  
inp_file=open("reviews.txt", "r") #input file
dic_file=inp_file.read() #read file
dict=eval(dic_file) #evaluate as dic from string
#print(type(dict))
ed=getsimilarity('Trevor Chappell','Peter') #call method1
print("Euclidean distance is %.4f" % ed) #format output
getsimilarities('Peter') #call method2
inp_file.close()#closr the file










    
     
    
    
    
