
import pandas as pd
import os
import nasdaqdatalink
import time

auth_tok = open("auth.txt","r").read()

#data = nasdaqdatalink.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken = auth_tok)

#print(data["Adj. Close"])

#path = "C:/Adams/Python/StockAnalyzer"
path = "C:/Adams/Python/StockAnalyzer/intraQuarter"

FEATURES =  ['Open',
             'High',
             'Low',
             'Close',
             'Volume',
             'Ex-Dividend',
             'Split Ratio',
             'Adj. Open',
             'Adj. High',
             'Adj. Low',
             'Adj. Close',
             'Adj. Volume']


def Stock_Prices():
    df = pd.DataFrame()
    #statspath = path+"/nasdaq_screener_3-25-2022.csv"
    #ticker_file = pd.read_csv(statspath)
    #stock_list = [x for x in ticker_file["Symbol"]]
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    print((stock_list))

    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("\\")[1]
            print(ticker)
            name = "WIKI/"+ticker.upper()
            data = nasdaqdatalink.get(name,
                                      trim_start = "2013-12-12",
                                      trim_end = "2018-12-30",
                                      authtoken = auth_tok)
            data[ticker.upper()] = data[FEATURES]
            df = pd.concat([df, data[ticker.upper()]], axis=1)
            #data = data[FEATURES]
            #print(data)
            #df = pd.concat([df, data], axis = 1) needs ticker
            #print(df)
        except Exception as e:
            try:
                time.sleep(5)
                print(str(e))
                ticker = each_dir.split("\\")[1]
                print(ticker)
                name = "WIKI/" + ticker.upper()
                data = nasdaqdatalink.get(name,
                                          trim_start="2013-12-12",
                                          trim_end="2018-12-30",
                                          authtoken=auth_tok)
                data[ticker.upper()] = data[FEATURES]
                df = pd.concat([df, data[ticker.upper()]], axis=1)
            except Exception as e:
                print(f"{ticker} not imported",str(e))

    df.to_csv("stock_prices_.csv")

Stock_Prices()