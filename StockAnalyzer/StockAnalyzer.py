
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
import statistics
style.use("ggplot")

'''FEATURES =  [#'Date',
             #'Ticker',
             'Price',
             'stock_p_change',
             'Status']'''

FEATURES =  ['DE Ratio',
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
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']

def Build_Data_Set():
    #data_df = pd.read_csv("sample_data_short.csv")
    data_df = pd.read_csv("key_stats_acc_perf_NO_NA_enhanced.csv")

    #data_df = data_df[:50]
    #data_df = data_df.reindex(np.random.permutation(data_df.index))
    #data_df = data_df.replace("NaN",0).replace("N/A",0)
    data_df = data_df.fillna(0)
    #data_df.index = range(len(data_df))

    X = np.array(data_df[FEATURES].values)#.tolist())

    y = (data_df["Status"]
         .replace("underperform",0))\
        .replace("outperform",1)\
        .values.tolist()

    X = preprocessing.scale(X)

    #Z = np.array(data_df[['stock_p_change']])
    Z = np.array(data_df[['stock_p_change','sp500_p_change', 'Enterprise Value/EBITDA', 'Held by Institutions', 'Short Ratio', 'Short % of Float',
                          'Ticker']])
    #tick = data_df["Ticker"].values.tolist()
    #tick = np.unique(tick)
    #print(tick)

    #print(X,y)
    return X,y,Z

def Analysis():
    test_size = 5789

    invest_amount = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0

    X, y, Z = Build_Data_Set()
    print(len(X))

    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X[:-test_size],y[:-test_size])

    correct_count, inc, dec = 0, 0, 0
    invest_list = []
    temp1, temp2, temp3, temp4, no_list = [], [], [], [], []

    for x in range(1, test_size):
        if clf.predict(X[[-x]])[0] == y[-x]:
            correct_count += 1
        '''if clf.predict(X[[-x]])[0] == 1:
            invest_return = invest_amount + (invest_amount * (Z[-x][0]/100))
            market_return = invest_amount + (invest_amount * (Z[-x][1]/100))
            temp1.append(Z[-x][2])
            temp2.append(Z[-x][3])
            temp3.append(Z[-x][4])
            temp4.append(Z[-x][5])
            total_invests += 1
            if_market += market_return
            if_strat += invest_return
            #invest_list.append(tick[-x])
            invest_list.append(Z[-x][6])
        else:
            no_list.append(Z[-x][6])'''
        if Z[-x][2] > 25:
            invest_return = invest_amount + (invest_amount * (Z[-x][0] / 100))
            market_return = invest_amount + (invest_amount * (Z[-x][1] / 100))
            total_invests += 1
            if_market += market_return
            if_strat += invest_return
            if invest_return > market_return:
                inc += 1
            else:
                dec += 1
            # invest_list.append(tick[-x])
            invest_list.append(Z[-x][6])

    print("Accuracy:", (correct_count/test_size) * 100.00)

    print("Total Trades:", total_invests)
    print("Ending with Strategy:",if_strat)
    print("Ending with Market:",if_market)
    profit = if_strat - if_market
    pct_inc = float(profit / if_market)*100
    print(f"Profit: {profit}\nPercent Increase: {pct_inc}%")
    #print('DE Ratio:',temp1)
    #print('Trailing P/E',temp2)
    #print('Price/Sales',temp3)
    #print('Price/Book',temp4)
    print(len(invest_list))
    print(invest_list)
    invest_list = np.unique(invest_list)
    no_list = np.unique(no_list)
    print(f"Increase: {inc}\nDecrease: {dec}\nAccuracy: {inc / (inc+dec)}")
    print(f"Green: {len(invest_list)}\nRed: {len(no_list)}")

    #for each_ticker in tick:
    #x_list, y_list, color_list = [], [], []
    '''test_good = []
    fig, ax = plt.subplots()
    for x in range(1, test_size):
        try:
            #plot_df = df[(df['Ticker'] == each_ticker)]
            #plot_df = plot_df.set_index(['Date'])
            ticker = Z[-x][6]
            data_viewing = Z[-x][2]
            #print(ticker)
            #print(de_ratio)

            if ticker in invest_list:
                color = 'g'
            else:
                color = 'r'

            if data_viewing > 25:
                test_good.append(ticker)
            #x_list.append(ticker)
            #y_list.append(de_ratio)
            #color_list.append(color)
            #plt.plot(ticker, de_ratio, label=ticker, color=color)
            #ax.scatter(ticker, data_viewing, color=color)
        except:
            pass

    test_good = np.unique(test_good)
    correct, incorrect = 0, 0
    print("Test Good:",len(test_good))
    for test in test_good:
        if test in invest_list:
            correct += 1
        else:
            incorrect += 1
    print("Correct:",correct,"\nIncorrect:",incorrect)'''
    #ticker_list = np.unique(x_list)
    #plt.plot(x_list, y_list, color=color_list)
    #plt.legend()
    #plt.show()

    #compared = ((if_strat - if_market) / if_market) * 100.0
    #do_nothing = total_invests * invest_amount

    #avg_market = ((if_market - do_nothing) / do_nothing) * 100.0
    #avg_strat = ((if_strat - do_nothing) / do_nothing) * 100.0

    #print("Compared to market, we earn",str(compared)+"% more")
    #print("Average investment return:", str(avg_strat)+"%")
    #print("Average market return:", str(avg_market)+"%")

    '''data_df = pd.read_csv("forward_sample_NO_NA.csv")
    print(data_df)

    #data_df = data_df.replace("N/A",0).replace("NaN",0)
    data_df = data_df.fillna(0)

    X = np.array(data_df[FEATURES].values)# .tolist())

    X = preprocessing.scale(X)

    Z = data_df["Ticker"].values.tolist()

    invest_list = []

    for i in range(len(X)):
        p = clf.predict(X[[i]])[0]
        if p == 1:
            print(Z[i])
            invest_list.append(Z[i])

    print(len(invest_list))
    print(invest_list)'''


Analysis()
