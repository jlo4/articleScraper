import requests
import re
import string
import mysql.connector
from bs4 import BeautifulSoup

homePage = requests.get("https://selkosanomat.fi/")
soup = BeautifulSoup(homePage.content)

articles = soup.findAll("article", {"class": "etusivu"})

##for article in articles:
##    link = article.a.get('href')
##    print(link)
##
firstArticleLink = articles[0].a.get('href')

firstArticle = requests.get("https://selkosanomat.fi" + firstArticleLink)

articleSoup = BeautifulSoup(firstArticle.content)

fullArticle = articleSoup.find("div", {"id": "content"})

text = fullArticle.find("div", {"class": "entry-content"})

pTags = text.findAll("p")

##for tag in pTags:
##   print(tag.text)

##text = 'Poliisit poliisit ovat tiukentaneet joulutorien valvontaa Ranskassa. ovat ovat '
##articleList = re.sub(r'[^\w\s]', '', text, re.UNICODE)
exclude = set(string.punctuation)

toPrint = ''
for tag in pTags:
    for ch in tag.text:
        if ch not in exclude:
            toPrint = toPrint + ch.lower().replace('\n', ' ')
    
listToPrint = []
for word in toPrint.split():
    if word in listToPrint:
        continue
    else:
        listToPrint.append(word)

##for w in listToPrint:
##    print(w)
