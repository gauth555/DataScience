# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 15:52:25 2015

@author: manghnani
"""

import os
import string
import re
import nltk

os.chdir('C:/Users/manghnani/Documents/Python Scripts/Assignment - 3')

score_dict={}
#dictionary for scores
fopen=open("AFINN-111.txt","r")
for counter in fopen:
    words_calculate=counter.split()
    a=counter[:counter.index('\t')]
    b=counter[counter.index('\t')+1:-1]
    score_dict[a]=b
  
# Reading the tweets file and make a dictionary from it
fhandle=open("cwctweets.txt","r")
file_input=fhandle.readlines()
list_a=[]
for line in file_input:
    #Use the eval function to convert each and every line to a dictionary
    fd=eval(line)
    #Append it to a list 
    list_a.append(fd)
fhandle.close()

list_string=[]
for d in list_a:
    list_string.append(d['statuses'])

text=[]
location=[]
hashtags=[]

tweet_loc_dict={}
tweet_name_dict={}
retweet_count_dict={}
for i in list_string:
    for counter_2 in i:#string_lists has list of dictionaries
        
        if 'text' in counter_2:
            if 'text':
#From each status get the text. Here, text is a key 
                text.append(counter_2['text'])

        key_list_j=list(counter_2.keys())
        
        if 'retweet_count' in counter_2:
            rtweet=counter_2['retweet_count']
            retweet_count_dict[counter_2['text']]=rtweet        

        # User is a key. 
        
        if 'user' in key_list_j:
            k=counter_2['user']

#Inside 'User' we have another dictionary where 'location' is a key
       
            if 'location' in k:
                    if k['location']:
                        l=k['location']
                        tweet_loc_dict[counter_2['text']]=l
                        location.append(l)        
        
        if 'entities' in counter_2:#under each status; then look at 'hashtags' under 'entities' 
            if 'hashtags' in counter_2['entities']:
                for a in counter_2['entities']['hashtags']:
                    h=a['text']
                    hashtags.append(h)
                for n in counter_2['entities']['user_mentions']:
                    name=n['name']
                    tweet_name_dict[counter_2['text']]=name


txt=''.join(text)
p=string.punctuation
d=string.digits
table=str.maketrans(p, len(p) * " ")#remove punctuation
txt=txt.translate(table)
table=str.maketrans(d, len(d) * " ")#remove digits
txt=txt.translate(table)

#create a list of stop words and stop lists
codelist=['/r','/n','/t']
more_stop_words=['cant','didnt','doesnt','dont','goes','isnt','hes',\
'shes','thats','theres','theyre','wont','youll','youre','youve',\
're','tv','g','us','en','ve','vg','didn','pg','gp','our','we',
'll','film','video','name','years','days','one','two','three',\
'four','five','six','seven','eight','nine','ten','eleven','twelve','http','rt','co','amp'] 



stoplist=nltk.corpus.stopwords.words('english')+more_stop_words

def text_parse(txt):
    txt=txt.lower()
    txt=re.sub('[^a-zA-Z]',' ',txt)#anything that doesnt begin with an alphabet is removed
    for i in range(len(codelist)):
        stopstring=' '+codelist[i]+' ' 
        txt=re.sub(stopstring,' ',txt)#stop words are removed
    for i in stoplist:
        stopstring=' '+i+' '
        txt=re.sub(stopstring,' ',txt)
    txt=re.sub('\s.\s',' ',txt)#single letter words removed
    txt=re.sub('\s+',' ',txt)#multiple spaces replaced with single space
    txt=txt.strip()
    return txt

txt=text_parse(txt)#call parse function    
    
    
f=open("text.txt","w") 
f.write(txt)

#Create a frequency plot of the top 25 words 
#hint: use nltk.FreqDist 

f=open('text.txt')
words = nltk.word_tokenize(f.read())
freq = nltk.FreqDist(words)#freqeuncy distribution of words
freq.plot(25)#plot of 25 words

#print(nltk.FreqDist(hashtags).most_common(25))

text_p=[]
tweet_score={}
for i in text:
    i_p=text_parse(i)
    tweet_l=i_p.split(' ')#every word in the tweet is put into a list
    score=0
    for word in tweet_l:      
        if word in score_dict:
            score=score+eval(score_dict[word])
    tweet_score[i]=score

#Display the total sentiment score for each tweet 
#output should be in the following format: 
#Record# Tweet  User  location  retweets   Sentiment Score 
final_data={}
tweet=[]
user=[]
loc=[]
retweets=[]
score=[]
ind=[]
count=0
#create an empty lists and append list in the order in which the text appears, if not found, append NA
for keys in text:
    count+=1
    ind.append(count)
    tweet.append(keys)
    if keys in tweet_name_dict:
        user.append(tweet_name_dict[keys])
    else:
        user.append('NA')
    if keys in tweet_loc_dict:
        loc.append(tweet_loc_dict[keys])     
    else:
        loc.append('NA')
    score.append(tweet_score[keys]) 
    if keys in retweet_count_dict:
        retweets.append(retweet_count_dict[keys])
    else:
        retweets.append('NA')

#append those lists to the dictionary final_data created
        
final_data['1. Record#']=ind
final_data['2. Tweet']=tweet
final_data['3. User']=user
final_data['4. Location']=loc
final_data['5. Retweets']=retweets
final_data['6. Sentiment']=score

#import operator
#final_data = sorted(final_data.items(), key=operator.itemgetter(0))
# Using Pandas
import pandas as pd
#create dictionary into data frame
table=pd.DataFrame(final_data)
print(table)
#table.index.rename('Record#', inplace=True)
table.to_excel('tweets_cwc.xlsx')
table=pd.read_excel('tweets_cwc.xlsx')

print(table)