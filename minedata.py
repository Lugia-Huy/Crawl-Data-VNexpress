import re
import csv
import validators
import pandas as pd
import random
from newspaper import Article
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer


def is_url(url):
    return validators.url(url)

def mine(url):
    article = Article(url)
    article.download()
    article.parse()
    data = []
    #url, title, keyword, content
    data.append( [url, article.title,
              ', '.join(article.keywords
                if article.keywords
                else (article.meta_keywords
                      if article.meta_keywords
                      else article.meta_data.get('keywords', []))),
                re.sub('\\n+', ' ', article.text)
              ])
    return data

#######
print("Please choice topic's file: ")
topic = input()

file_name = topic+'.csv'
df = pd.read_csv(file_name, header=None, encoding='utf-16')
array = df.values
Link = array[:, 1]
k = len(Link)
#random link
data = mine(Link[random.choice(range(k))])
title = []
title.append(data[0][1])

keywords = []
keywords.append(data[0][2])

contents = []
contents.append(data[0][3])

tokenize = sent_tokenize(str(contents[0]))
vec = CountVectorizer()
X = vec.fit_transform(tokenize)

with open('keywords.csv', 'w', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(keywords)

with open('tokenize.csv', 'w', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(tokenize)

with open('CountVectorizer.csv', 'w', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(X)
