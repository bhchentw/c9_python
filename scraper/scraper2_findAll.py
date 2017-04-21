
"""
到網頁抓出綠色的字
使用到的重點是findAll

"""
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"

print()
namelist = bsObj.findAll("span",{"class":"green"}) #findAll(tag,attributes,recursive,text,limit,keyboards)
for name in namelist:
    print(name.get_text())

