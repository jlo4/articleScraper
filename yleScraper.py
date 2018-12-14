import requests
from bs4 import BeautifulSoup

homePage = requests.get("https://svenska.yle.fi/inrikes")
soup = BeautifulSoup(homePage.content)

articles = soup.findAll("article", {"class": "ydd-teaser-list__wrapper"})

for article in articles:
    link = article.a.get('href')
    print(link)

