
"""
 這個程式非常的簡潔, 
 python 有非常多各個專業領域的package可供下戴, 只要import需要的module 便可focus在要處理的問題而不是程式本身
 
 package ______ module a
          |____ module b
          .....
          |____ module n
          
 urllib.request 與 bs4都是 package (底下具有多個module)
 
 urllib.request裡的 urlopen 去 "https://pythonscraping.com/pages/page1.html" 抓完整的html檔 並存進html這個變數
 bs4 裡的 BeautifulSoup 再將html裡的網頁資料分門別類的存在 bsObj這個物件, 按我們的需求可提取出需要的html code
 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://pythonscraping.com/pages/page1.html") #書的範例網址 裡面寫的文字我都看不懂
print("印出上述網頁完整的html文字檔=",html.read())

html=urlopen("https://pythonscraping.com/pages/page1.html")  # 這行沒重寫下面會讀不到, html只能用一次
bsObj=BeautifulSoup(html.read(),"html5lib") # update BeautifulSoup using with argument "html5lib"
print()
print("html裡的h1層抓出來=",bsObj.h1)