# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 23:06:47 2015

@author: manghnani
"""
# Assignment 1
# Prompting the User to enter the directory
import os
import random
dir=input("Enter Dir:")
os.chdir(dir)
# Reading the file words.txt and then saving the contents into my_file variable
my_file=open("words.txt","r")
#print(type(my_file))

#Creating a dictionary and then moving the contents from the file into the dict
dictionary1={}

for line in my_file:
    x=line.split(":")
    a=x[0]
    b=x[1]
    c=len(b)-1 # The -1 gets the lenght of b minus'\n'
    b=b[0:c] # from element zero upto but not including the '\n'
    dictionary1[a]=b

#Extracting the Keys from the dictionary and saving it in a list variable
words=list(dictionary1.keys())

# Define a function to scramble the word
def scramble(w):
    lst=list(w)
    random.shuffle(lst)
    new_word=''.join(lst)
    return new_word
    
# Checking if the word that the user inputs is the same as the scrambled word

while True: # Anything that is non zero is considered true
    word=random.choice(words)
    scrambled_word=scramble(word)
    users_input=input("Unscramble the letters to form the word" \
    "\n Type '?' for the meaning of the unscrambled word \n" \
    +scrambled_word+ " : ")
    while users_input!=word:
        if users_input=='?':
            print("The word means :" +dictionary1[word])
            users_input=input("Unscramble the letters to form the word"\
                        "\n Type '?' for the meaning of the unscrambled word \n"
                        +scrambled_word+ ":")
                        
        else:
            print("You got it wrong! Please try again!")
            users_input=input("Unscramble the letters to form the word"\
                        "\n Type '?' for the meaning of the unscrambled word \n"
                        +scrambled_word+ ":")

    if users_input==word:
        user_response=input("You got it! Do you want to continue [yes or no]:")
        if user_response=='yes':
            continue
        else:
            break 
            # This break is used to exit the loop. 
            #In this case it is the for statement [NOT an if statement]
        
    else:
        print("You got it wrong! Please try again!")
        continue