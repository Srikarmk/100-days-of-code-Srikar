from bs4 import BeautifulSoup

with open('scrape.html','r') as html_f:
    content=html_f.read()


soup=BeautifulSoup(content,'lxml')
# tag=soup.find('li')
tag=soup.find_all('li')
print(tag)