
"""
beautifulsoup 用到的 function ==> next_sibling, previous_sibling
介紹如下
https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#next-sibling-previous-sibling
"""
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
print(time.ctime())
#print(time.asctime(time.time()))
html=urlopen("https://pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"
print()

for sibling in bsObj.find("table",{"id":"giftList"}).tr.previous_siblings:
    print(sibling)
