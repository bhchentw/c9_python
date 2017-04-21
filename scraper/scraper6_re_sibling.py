

"""
beautifulsoup 用到的 function ==> next_sibling, previous_sibling
介紹如下
https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#next-sibling-previous-sibling
"""
import time
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
print(time.ctime())
#print(time.asctime(time.time()))
html=urlopen("https://pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"html5lib") # update BeautifulSoup using with argument "html5lib"
print()




for sibling in bsObj.findAll("tr",{"id":re.compile("gift*")}): # find each <tr> with id = gift1,2,3,4,5
    for sibling2 in sibling.findAll(text=re.compile("\$")):  #用findAll 的 text 配上正規化 \ 跳脫, sibling2 is the price now
        print(sibling2.parent.previous_sibling.previous_sibling.get_text(),sibling2) # get_text()  can remove the <td>.....</td>

'''
    td
       item
    td
       description
    td 
       price
       
    so when we got the "price", we can also get the "item" through parent -> previous_sibling -> previous_sibling
'''