#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Experiment 2: Implement the concepts of Stemming & Lemmatization

#Stemming
import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

print(ps.stem("batting"));
print(ps.stem("batsman"));
print(ps.stem("Going"));


# In[2]:


#Lemmtization
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("rocks :", lemmatizer.lemmatize("rocks"))


# In[ ]:




