"""
  css selector
  和其它學到的都很像, 不過好像比較直接一點
  參考以下連結
  https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#css    
"""

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

#html=urlopen("https://pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html_doc,"html5lib") # update BeautifulSoup using with argument "html5lib"
print()


#print(  ( bsObj.select("html body p") )  )

for bs_list in bsObj.select(" .sister"):  #    id=> #id,  class=> .class, href=> [href]
    print(bs_list)
    print()

#print(  ( bsObj.select("tr td") )  )


