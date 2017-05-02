"""
抓三大法人買賣金額統計表, 可自行修改日期在form_data裡的qdate
原先利用get的方法只能抓到最新一天的資料, 參考blog修改以下版本
http://chentain.pixnet.net/blog/post/44814997
程式後有原文備份

2017.4.30
V2 更新
可以抓連續多個日期
getTradeValue(yyy/mm/dd) 可回傳三大法人資料

2017.5.1
輸出格式小改版

2017.5.3   V2.1
新增 def money_conversion(in_ele)
將金額字串轉換成數字並將千位分隔符號去掉
"""

from datetime  import date,timedelta
import sqlite3 as lite
import requests
import urllib
from bs4 import BeautifulSoup


form_data = { #修改qdate可更改時間
    "queryDWM":"by_issueD",
    "qdate":"106/04/25",   
    "query_yearW":"2017",
    "query_week":"20170424",
    "query_yearM":"2017",
    "query_monthM":"4"
}


url = 'http://www.tse.com.tw/ch/trading/fund/BFI82U/BFI82U.php'
sql = "insert into InvestorTradingValue(item,total_buy,total_sell,difference,date) values('foreign',20,30,10,'2017-5-2')"

def money_conversion(in_ele): #convert abc,def,ghi (in string) ==> abcdefghi (in integer)
    return int(''.join(in_ele.split(',')))
    
def getTradeValue(cur,date_get):    
    
    day_array = str(date_get).split('-')
    day_str = [str(int(day_array[0])-1911), day_array[1],day_array[2]]
    day_format = '/'.join(day_str)
    
    form_data.update(qdate=day_format)
    #print(form_data)
    data = urllib.parse.urlencode(form_data).encode("utf-8") # 後面要加上 .encode("utf-8")
    req = urllib.request.Request(url,data)
    html = urllib.request.urlopen(req)
    
    bsObj=BeautifulSoup(html.read(),"html5lib") # update BeautifulSoup using with argument "html5lib"
    table = bsObj.select("table tr") # table tbody tr
    table = table[2:]
    for tr in table:
        td = tr.select("td")
        print(td[0].text,money_conversion(td[1].text),money_conversion(td[2].text),money_conversion(td[3].text), date_get )   
        #print(ele.text)
    #table = table[2:]
    #namelist = bsObj.table.findAll("td")#,{"style":"text-align:right"})
    #print(namelist)
    #for name in namelist:
    #    print(name.text)
    
   



con = lite.connect('finance.sqlite')
cur = con.cursor()
cur.execute(sql)
con.commit()

#cur.execute("select * from InvestorTradingValue")

today = date.today()
#print(today)
for i in range(1,2):
    print(  today   )
    #getTradeValue('106/04/27') 
    getTradeValue(cur,today) 
    today = today + timedelta(days=-1)
ret = cur.fetchone()
con.close()
