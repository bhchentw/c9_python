
"""
beautifulsoup 用到的 function ==> children, contents, descendants
介紹如下
https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#contents-children

"""
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
print(time.ctime())
html=urlopen("https://pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"
print()

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
