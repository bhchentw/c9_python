"""
用正規化的方式將img檔抓南, 最後的src是 img的屬性
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("https://pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
   

