# not finished
import pandas as pd
import os
import time
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
import re

path = "C:/Adams/Python/StockAnalyzer/intraQuarter"

def Key_Stats():
    #statspath = path+'/_KeyStats'
    #stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)
    df = pd.DataFrame(columns = ['Date',
                                 #'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 #'SP500',
                                 #'sp500_p_change',
                                 #'Difference',
                                 ##############
                                 'Status'])

    #sp500_df = pd.read_csv("YAHOO-INDEX_GSPC.csv")
    stock_df = pd.read_csv("stock_prices_.csv")
    #print(stock_df)
    ticker_list = list(stock_df.columns)[1:]
    date_list = list(stock_df["Date"])[:-1]
    print(len(ticker_list))
    print(len(date_list))
    for i in range(len(ticker_list)):
        #print(stock_df)
        ticker = ticker_list[i]
        print(ticker)
        #each_file = os.listdir(each_dir)
        #print(each_file)
        #ticker = each_dir.split("\\")[1]
        #ticker_list.append(ticker)
        #print(ticker_list)

        #starting_stock_value = False
        #starting_sp500_value = False
        for j in range(int(len(date_list)/12)):
            #print(stock_df["Date"][j])
            cur_date = stock_df["Date"][j*12]
            #if len(stock_df.rows) > 0:
            #for item in rows[1]:
            #print(item)
            date_stamp = datetime.strptime(cur_date, '%m/%d/%Y').date()
            unix_time = time.mktime(date_stamp.timetuple())
            date_stamp = date_stamp.strftime('%m/%d/%Y')
            #print(date_stamp, unix_time)
            #full_file_path = each_dir+'/'+file
            #print(full_file_path)
            #source = open(full_file_path,'r').read()
            #print(source)
            try:
                value_list = []

                '''for each_data in gather:
                    try:
                        regex = re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'
                        value = re.search(regex, source)
                        value = (value.group(1))
                        #value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                        #value = float(source.split(gather + ':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                        if "B" in value:
                            value = float(value.replace("B",''))*1000000000
                        if "M" in value:
                            value = float(value.replace("B",''))*1000000

                        value_list.append(value)
                        #print(value_list)
                    except Exception as e:
                        value = "0"
                        value_list.append(value)'''

                one_year_later = int(unix_time + 31536000)

                try:
                    stock_price_1y = datetime.fromtimestamp(one_year_later).strftime('%m/%d/%Y')
                    #print(stock_price_1y)
                    #stock_loc = stock_df.loc[stock_df.isin([stock_price_1y]).any(axis=1)].index.tolist()
                    row = stock_df[stock_df['Date'][stock_df.index] == stock_price_1y][ticker.upper()]
                    #print(stock_df[stock_price_1y])
                    #print(row)
                    stock_1y_value = round(float(row), 2)
                    #print(stock_1y_value)
                except Exception as e:
                    try:
                        stock_price_1y = datetime.fromtimestamp(one_year_later-259200).strftime('%m/%d/%Y')
                        #row = stock_df[(stock_df["Unnamed: 0"][stock_df.index] == stock_price_1y)][ticker.upper()]
                        row = stock_df[stock_df['Date'][stock_df.index] == stock_price_1y][ticker.upper()]
                        stock_1y_value = round(float(row),2)
                    except Exception as e:
                        print("stock price:", str(e))

                try:
                    stock_price = datetime.fromtimestamp(unix_time).strftime('%m/%d/%Y')
                    row = stock_df[(stock_df["Date"][stock_df.index] == stock_price)][ticker.upper()]
                    stock_price = round(float(row), 2)
                except Exception as e:
                    try:
                        stock_price = datetime.fromtimestamp(unix_time-259200).strftime('%m/%d/%Y')
                        row = stock_df[(stock_df["Date"][stock_df.index] == stock_price)][ticker.upper()]
                        stock_price = round(float(row), 2)
                    except Exception as e:
                        print("stock price:", str(e))

                stock_p_change = round((((stock_1y_value - stock_price) / stock_price) * 100),2)
                #sp500_p_change = round((((sp500_1y_value - sp500_value) / sp500_value) * 100),2)

                #difference = stock_p_change-sp500_p_change

                if stock_p_change > 5:
                    status = 1
                else:
                    status = 0

                if value_list.count("N/A") > 0:
                    #print(value_list)
                    pass
                else:

                    df = df.append({'Date':date_stamp,
                                        'Ticker':ticker,
                                        'Price':stock_price,
                                        'stock_p_change':stock_p_change,
                                        'Status':status}, ignore_index = True)
            except Exception as e:
                pass


    df.to_csv("sample_data_short.csv")

Key_Stats()