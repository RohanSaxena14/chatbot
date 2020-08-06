
from bs4 import BeautifulSoup as bs
import requests as req
from pprint import pprint
import sys
sys.path.append('/home/maheep/nlp/lib/python3.6/site-packages')
import nltk
import numpy as np
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import codecs

dfile = open('./my.txt','r')
content = dfile.read()

sent_tokens = content.split("\n")
print(len(sent_tokens))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

lemmatizer = nltk.WordNetLemmatizer()

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

cleaned_text = []
'''
def preprocess(sent_tokens):
for sentence in sent_tokens:
    words_arr = nltk.word_tokenize(sentence)
    cleaned_text.append(" ".join(f for f in [lemmatizer.lemmatize(y.lower()) for y in words_arr if y.isalnum()]))
return cleaned_text  
'''  
def response():

    bot_response = ''
    TfidfVec = TfidfVectorizer(stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    value = cosine_similarity(tfidf[-1][:5],tfidf)
    idx=value.argsort()[0][-2]
    tfidf_value = value[0][idx]

    if tfidf_value!=0:
        bot_response = sent_tokens[idx]

    else:
        bot_response = "Sorry I did not understood your question"
    return bot_response


print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
def answer_of_query(user_response):
    flag=True
    while(flag==True):
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                return("ROBO: You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    return greeting(user_response)
                else:
                    print(np.array(sent_tokens).shape)
                    sent_tokens.append(user_response)
                    print("ROBO: ",end="")
                    r = response()
                    sent_tokens.remove(user_response)
                    return r
        else:
            flag=False
            return("ROBO: Bye! take care..")





