# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 08:12:02 2015

@author: manghnani
"""


#current working directory
import os
os.chdir("C:/Users/manghnani/Documents/Python Scripts/Assignment - 3/files")

#from __future__ import print_function
lis=[]
count=0
list_corpus=[]
corpus=''

import glob
# reading all the files and then append it to a list
for file in glob.glob("*.txt"):
    file_input=open(file,'r')
    f_read=file_input.read()
    corpus=corpus+f_read
    list_corpus.append(f_read)
    
#Remove stop words
import nltk   
codelist=['\n','\t','\r']
more_stop_words=['cant','didnt','doesnt','dont','goes','isnt','hes',\
'shes','thats','theres','theyre','wont','youll','youre','youve',\
're','tv','g','us','en','ve','vg','didn','pg','gp','our','we',
'll','text','video','name','ta','fr','years','days','one','two','three',\
'four','five','six','pdf','seven','eight','nine','ten','eleven','twelve',\
'et','al','also','may','vol','ii','pm','thus','crossref']
stoplist=nltk.corpus.stopwords.words('english')+more_stop_words

#Function to process the corpus- parse and remove punctuation, digits

import string
def remove_p_d(corpus):
    p=string.punctuation
    d=string.digits
    table=str.maketrans(p, len(p) * " ")
    corpus=corpus.translate(table)
    table=str.maketrans(d, len(d) * " ")
    corpus=corpus.translate(table)
    return corpus

#Function to process the corpus - spaces, single letter words

import re    
def remove_extra(corpus):
    corpus=corpus.lower()
    corpus=re.sub('[^a-zA-Z]',' ',corpus)
    for i in stoplist:
        stop_string=' '+i+' '
        corpus=re.sub(stop_string,' ',corpus)
    for i in range(len(codelist)):
        code_string=' '+codelist[i]+' '
        corpus=re.sub(code_string,' ',corpus)
    corpus=re.sub('\s.\s',' ',corpus)
    corpus=re.sub('\s..\s',' ',corpus) # Removing stray words of two character length
    corpus=re.sub('\s',' ',corpus)
    corpus=corpus.strip()
    corpus=re.sub('\s.\s',' ',corpus)
    return corpus
    

corpus=remove_p_d(corpus)
corpus=remove_extra(corpus)
corpus_doc_parsed=[]
for doc in list_corpus:
    doc=remove_p_d(doc)
    doc=remove_extra(doc)
    corpus_doc_parsed.append(doc)
    
#Generate the freqDist of the most frequent words from corpus

words=nltk.word_tokenize(corpus)
freq_words=nltk.FreqDist(words)
freq_words.plot(50)    

#topics

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

n_topics=8 #Select any 8 topics
n_top_words=15# From within the 8 topics choose top 10 words for each
n_samples=len(corpus_doc_parsed)
vectorizer=TfidfVectorizer()#convert the topic to a term document matrix
tfidf = vectorizer.fit_transform(corpus_doc_parsed)
#initialize the NMF constructor
nmf_vect=NMF(n_components=n_topics, max_iter = 1000, random_state=1)
nmf = nmf_vect.fit(tfidf)
#get the feature names- all words from term by document matrix
feature_names=vectorizer.get_feature_names()
n_features=len(feature_names)
#print(n_features)
#Here the value of n_features is 5
# Fit the NMF model
print('Fitting the NMF model with n_samples=%d and n_features=%d' % (n_samples, n_features))
for topic_idx, topic in enumerate(nmf.components_):
    topic_idx=int(topic_idx)+1
    print("Topic #%d:" % topic_idx)
    print(",".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()