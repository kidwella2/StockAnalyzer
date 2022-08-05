
# HTTP Error 404: Not Found, vid: 21/28
#import urllib3
import requests
#import urllib.request
import os
import time

path = "C:/Adams/Python/StockAnalyzer/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/71.0.3578.98 Safari/537.36'}

    for e in stock_list[1:]:
        try:
            e = e.replace("C:/Adams/Python/StockAnalyzer/intraQuarter/_KeyStats\\","")
            #link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            #link = "http://finance.yahoo.com/quote/"+e.upper()+"/key-statistics?ltr=1"
            print(e)
            link = "https://finance.yahoo.com/quote/" + e.upper() + "/key-statistics?p=" + e.upper()
            print(link)
            #if link.lower().startswith('http'):
                #resp = urllib.request.urlopen(link).read()
            #else:
                #raise ValueError from None
            #http = urllib3.PoolManager()
            try:
                #resp = http.request("GET", link)
                resp = requests.get(link, headers=headers, timeout=5).text
                #print(resp)
                #print(resp.data)
                #htmlBytes = response.read()
                #print(type(htmlBytes))
            except Exception as e:
                print(str(e))


            #htmlStr = htmlBytes.decode("utf8")
            #print(type(htmlStr))

            save = path+"/forward/"+str(e)+".html"
            print(save)
            store = open(save,"w")
            store.write(str(resp))
            store.close()
        except Exception as e:
            print(str(e))
            time.sleep(2)

Check_Yahoo()