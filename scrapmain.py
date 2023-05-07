from functions import *

from bs4 import BeautifulSoup 


import requests

page_main=requests.get('https://groww.in/stocks/exide-industries-ltd')
print(page_main)
# soup=BeautifulSoup(page_main,'lxml')
# j=soup.find('span',class_='lpu38Pri fs28 ')
# print(j)
