from bs4 import BeautifulSoup

with open('scrape.html','r') as html_f:
    content=html_f.read()


soup=BeautifulSoup(content,'lxml')
# tag=soup.find('li')
tags=soup.find_all('li')

for tag in tags:
    print(tag.text)