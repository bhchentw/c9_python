
"""
抓三大法人買賣金額統計表, 可自行修改日期在form_data裡的qdate
原先利用get的方法只能抓到最新一天的資料, 參考blog修改以下版本
http://chentain.pixnet.net/blog/post/44814997
程式後有原文備份

V2 更新
可以抓連續多個日期
getTradeValue(yyy/mm/dd) 可回傳資料
"""

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

def getTradeValue(date_get):
    form_data.update(qdate=date_get)
    print(form_data)
    data = urllib.parse.urlencode(form_data).encode("utf-8") # 後面要加上 .encode("utf-8")
    req = urllib.request.Request(url,data)
    html = urllib.request.urlopen(req)
    
    bsObj=BeautifulSoup(html.read(),"html5lib") # update BeautifulSoup using with argument "html5lib"
    table = bsObj.select("table tr")
    table = table[2:]
    namelist = bsObj.table.findAll("td")#,{"style":"text-align:right"})
    
    for name in namelist:
        print(name.text)
    
   


from datetime  import date,timedelta
today = date.today()
for i in range(1,10):
    today = today + timedelta(days=-1)
    day_array = str(today).split('-')
    day_str = [str(int(day_array[0])-1911), day_array[1],day_array[2]]
    day_format = '/'.join(day_str)
    getTradeValue(day_format) 
    #print(  day_format    )
