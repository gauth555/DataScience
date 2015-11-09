# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 15:07:13 2015

@author: manghnani
"""
import re #import regular expression for pattern selection
import random #import random module for random scrambling and choosing

def scramble(word): #function to scramble words
    word_list=list(word)#string converted to list
    random.shuffle(word_list)#list of characters is shuffled
    scram_word="".join(word_list)#shuffled words are created into a jumbled word
    return scram_word #returning the scrambled word
    

try:#try block to look for exceptions
    while True: #main loop
        dic={}#empty dictionary to store data
        inp_file=open("words.txt","r")#file opened
        w_file=inp_file.read()#read the file
        words=re.findall(r'(\w+):',w_file)#create a patter to find all the words that need to be scrambled- it occurs before ':' pattern
        words_dic=re.findall(r'(\w+):(.+)',w_file)#patter that creates tuples of words and their meanings - (word):(meanings)
        j=len(words_dic)
        for i in range(j):#accessing the created list of tuples and creating a dictionary from it
            m=words_dic[i][0]
            dic[m]=words_dic[i][1]#dic[] dictionary created with words and their meanings
            i+=1
        inp_file.close()#file closed
        #print('words to jumble: ',words,'\n\n\n')
        print("Unscramble the letters to form a word.\nType '?' for the meaning of the unscrambled word ")
        pick=random.choice(words)#randomly choosing a word to be scrambled from the word list
        guess=scramble(pick)#calling the function to jumble it
        print('\n\n\n',guess,'\n\n\n')
        #while True:
        option=input('Enter word [? for meaning of unscrambled word]:')#ask for user's answer or request for meaning
        while (option.lower()!=pick):#if answer provided is not the right word
            if option=='?':#if the option entered by the user is '?' for meaning
                print("The word means:" , dic[pick] )#pick out meaining from the dictionary dic
                print(guess)
                option=input('Enter word [? for meaning of unscrambled word]:')
                continue
            else:
                option=input('Enter word [? for meaning of unscrambled word]:')
                #incase the typed asnwer is not the right answers continue the loop till the right answer is provided
                
        if option.lower()==pick:
                option2=input('You got it! Do you want to continue [yes or no]: ' ) #if the answer is right
                if option2.lower()=='yes' or option2.lower()=='y':#if the user wants to continue playing back to the top of the while loop
                    continue
                elif option2.lower()=='n' or option2.lower()=='no':#exit if the user wants to discontinue
                    break
                  
                   
except:
        print("Exiting program with an error")#except block to look for handling error or displaying its cause
    
    
   