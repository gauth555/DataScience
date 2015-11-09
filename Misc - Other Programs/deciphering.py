# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:18:38 2015

@author: manghnani
"""
# Program to decipher the text
list_a='abcdefghijklmnopqrstuvwxyz' # Alphabets from a to z
list_a=list(list_a)# Converting the string into a list with every letter as a list element
# print (list_a)
before_deciphering='Yqwt jqogyqtm ku fwg vqpkijv' # Word to Decipher
# print(before_deciphering)
# Converting the string into a list of individual characters
list_b=list(before_deciphering)
# Removing out the first letter since it is capital case
first = list_b.pop(0)
# print (list_b)
# Comparing the elements in two lists 
after_deciphering=''
for char_in_list_b in list_b:
    for char_in_list_a in list_a:    
        if char_in_list_b == char_in_list_a:
            # print(char_in_list_b)            
            list_a_index=list_a.index(char_in_list_b) # Populate the index of list a
            # print(list_a_index)
            new_list_a_index=list_a_index-2 # Reducing the index by value 2
            # print(new_list_a_index)            
            l=list_a[new_list_a_index] # Populating the value of the index and storing it in a variable
            # print(l)            
            after_deciphering= after_deciphering + str(l) # appending the variable to form the string
            # print(after_deciphering)            
            #after_deciphering=after_deciphering.title()
            #print(after_deciphering)
        elif char_in_list_b == ' ': # Incase there are characters then include spaces in the resulting string
            after_deciphering= after_deciphering + ' '
            break
# Printing the string with after concatenating the first variable to the resultant variable
print("The string after deciphering is :",first + after_deciphering)