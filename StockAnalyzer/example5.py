
import pandas as pd
import os
import nasdaqdatalink
import time

auth_tok = open("auth.txt","r").read()

#data = nasdaqdatalink.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken = auth_tok)

#print(data["Adj. Close"])

path = "C:/Adams/Python/StockAnalyzer/intraQuarter"

def Stock_Prices():
    df = pd.DataFrame()
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("\\")[1]
            print(ticker)
            name = "WIKI/"+ticker.upper()
            data = nasdaqdatalink.get(name,
                                      trim_start = "2000-12-12",
                                      trim_end = "2014-12-30",
                                      authtoken = auth_tok)
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis = 1)
        except Exception as e:
            print(str(e))

    df.to_csv("stock_prices.csv")

Stock_Prices()