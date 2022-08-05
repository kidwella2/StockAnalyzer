
# Need example8.py data, vid: 22/28
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

def Forward(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                        'Enterprise Value',
                        'Forward P/E',
                        'PEG Ratio',        #
                        'Enterprise Value/Revenue',
                        'Enterprise Value/EBITDA',
                        '>Revenue<',
                        'Gross Profit',
                        '>EBITDA',
                        'Net Income Avi to Common',
                        'Diluted EPS',
                        'Earnings Growth',
                        'Revenue Growth',
                        'Total Cash',
                        'Total Cash Per Share',
                        'Total Debt',
                        'Current Ratio',
                        'Book Value Per Share',
                        'Operating Cash Flow',
                        'Levered Free Cash Flow',
                        'Beta',
                        'Held by Insiders',
                        'Held by Institutions',
                        'Shares Short (',
                        'Short Ratio',
                        'Short % of Float',
                        'Shares Short (prior ']):
    #statspath = path+'/_KeyStats'
    #stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 ##############
                                 'DE Ratio',
                                 'Trailing P/E',
                                 'Price/Sales',
                                 'Price/Book',
                                 'Profit Margin',
                                 'Operating Margin',
                                 'Return on Assets',
                                 'Return on Equity',
                                 'Revenue Per Share',
                                 'Market Cap',
                                 'Enterprise Value',
                                 'Forward P/E',
                                 'PEG Ratio',
                                 'Enterprise Value/Revenue',
                                 'Enterprise Value/EBITDA',
                                 'Revenue',
                                 'Gross Profit',
                                 'EBITDA',
                                 'Net Income Avi to Common',
                                 'Diluted EPS',
                                 'Earnings Growth',
                                 'Revenue Growth',
                                 'Total Cash',
                                 'Total Cash Per Share',
                                 'Total Debt',
                                 'Current Ratio',
                                 'Book Value Per Share',
                                 'Operating Cash Flow',
                                 'Levered Free Cash Flow',
                                 'Beta',
                                 'Held by Insiders',
                                 'Held by Institutions',
                                 'Shares Short (as of',
                                 'Short Ratio',
                                 'Short % of Float',
                                 'Shares Short (prior ',
                                 ##############
                                 'Status'])

    #sp500_df = pd.read_csv("YAHOO-INDEX_GSPC.csv")
    #stock_df = pd.read_csv("stock_prices.csv")
    #ticker_list = []
    file_list = os.listdir(path+"/forward")
    print(file_list)
    for each_file in file_list:
        #each_file = os.listdir(path+"/forward/"+each_file)
        print(each_file)
        ticker = each_file.split(".html")[0]
        full_file_path = path+"/forward/"+each_file
        source = open(full_file_path, "r").read()
        #ticker_list.append(ticker)

        #starting_stock_value = False
        #starting_sp500_value = False

        try:
            value_list = []

            for each_data in gather:
                try:
                    #each_data = [each_data]
                    regex = re.escape(each_data) + r'.*?(\d{1,8}\.?\d{1,8}M?B?|N/A)(</span>)?%?</td>'
                    #regex = re.escape(each_data) + r'</span> <!-- -->(mrq)<sup aria-label=""></sup></td><td class="Fw(500) Ta(end) Pstart(10px) Miw(60px)">(\d{1,8}M?B?|N/A)%?</td>'
                    #print(regex)
                    value = re.search(regex, source)
                    value = (value.group(1))
                    #value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    #value = float(source.split(gather + ':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    if "B" in value:
                        value = float(value.replace("B",''))*1000000000
                        value = str(value)
                    if "M" in value:
                        value = float(value.replace("M",''))*1000000
                        value = str(value)

                    value_list.append(value)
                except Exception as e:
                    print(e)
                    value = ""
                    value_list.append(value)

            if value_list.count("N/A") > 15:
                #print(value_list)
                pass
            else:


                df = df.append({'Date':"N/A",
                                    'Unix':"N/A",
                                    'Ticker':ticker,

                                    'Price':"N/A",
                                    'stock_p_change':"N/A",
                                    'SP500':"N/A",
                                    'sp500_p_change':"N/A",
                                    'Difference':"N/A",
                                    'DE Ratio':value_list[0],
                                    #'Market Cap':value_list[1],
                                    'Trailing P/E':value_list[1],
                                    'Price/Sales':value_list[2],
                                    'Price/Book':value_list[3],
                                    'Profit Margin':value_list[4],
                                    'Operating Margin':value_list[5],
                                    'Return on Assets':value_list[6],
                                    'Return on Equity':value_list[7],
                                    'Revenue Per Share':value_list[8],
                                    'Market Cap':value_list[9],
                                     'Enterprise Value':value_list[10],
                                     'Forward P/E':value_list[11],
                                     'PEG Ratio':value_list[12],
                                     'Enterprise Value/Revenue':value_list[13],
                                     'Enterprise Value/EBITDA':value_list[14],
                                     'Revenue':value_list[15],
                                     'Gross Profit':value_list[16],
                                     'EBITDA':value_list[17],
                                     'Net Income Avi to Common':value_list[18],
                                     'Diluted EPS':value_list[19],
                                     'Earnings Growth':value_list[20],
                                     'Revenue Growth':value_list[21],
                                     'Total Cash':value_list[22],
                                     'Total Cash Per Share':value_list[23],
                                     'Total Debt':value_list[24],
                                     'Current Ratio':value_list[25],
                                     'Book Value Per Share':value_list[26],
                                     'Operating Cash Flow':value_list[27],
                                     'Levered Free Cash Flow':value_list[28],
                                     'Beta':value_list[29],
                                     'Held by Insiders':value_list[30],
                                     'Held by Institutions':value_list[31],
                                     'Shares Short (as of':value_list[32],
                                     'Short Ratio':value_list[33],
                                     'Short % of Float':value_list[34],
                                     'Shares Short (prior ':value_list[35],
                                    'Status':"N/A"}, ignore_index = True)
        except Exception as e:
            pass
                    #print(str("e"))
                #print(ticker+":",value)
            #time.sleep(15)
    '''for each_ticker in ticker_list:
        try:
            plot_df = df[(df['Ticker'] == each_ticker)]
            plot_df = plot_df.set_index(['Date'])

            if plot_df['Status'][-1] == "underperform":
                color = 'r'
            else:
                color = 'g'

            plot_df['Difference'].plot(label=each_ticker, color=color)
            plt.legend()
        except:
            pass

    plt.show()'''

    #save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    #print(save)
    df.to_csv("forward_sample_WITH_NA.csv")

Forward()