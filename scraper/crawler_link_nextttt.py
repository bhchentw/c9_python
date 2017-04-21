"""
爬蟲前練習, 運用觀察及正規化找到目標連結
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())



html=urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"

links = bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
for link in links:
    if 'href' in link.attrs: #
        print(link.attrs['href'])
        #print(link)
   

