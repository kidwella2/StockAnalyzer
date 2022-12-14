
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
import statistics
style.use("ggplot")

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
    data_df = pd.read_csv("key_stats_acc_perf_WITH_NA_enhanced.csv")

    #data_df = data_df[:50]
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    #data_df = data_df.replace("NaN",0).replace("N/A",0)
    data_df = data_df.fillna(0)
    data_df.index = range(len(data_df))

    X = np.array(data_df[FEATURES].values)#.tolist())

    y = (data_df["Status"]
         .replace("underperform",0))\
        .replace("outperform",1)\
        .values.tolist()

    X = preprocessing.scale(X)

    Z = np.array(data_df[['stock_p_change','sp500_p_change']])
    tick = data_df["Ticker"].values.tolist()

    #print(X,y)
    return X,y,Z,tick

def Analysis():
    test_size = 1000

    invest_amount = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0

    X, y, Z, tick = Build_Data_Set()
    print(len(X))

    clf = svm.SVC(kernel="linear", C= 1.0)
    clf.fit(X[:-test_size],y[:-test_size])

    correct_count = 0
    invest_list = []

    for x in range(1, test_size):
        if clf.predict(X[[-x]])[0] == y[-x]:
            correct_count += 1
        if clf.predict(X[[-x]])[0] == 1:
            invest_return = invest_amount + (invest_amount * (Z[-x][0]/100))
            market_return = invest_amount + (invest_amount * (Z[-x][1] / 100))
            total_invests += 1
            if_market += market_return
            if_strat += invest_return
            invest_list.append(tick[-x])

    print("Accuracy:", (correct_count/test_size) * 100.00)

    print("Total Trades:", total_invests)
    print("Ending with Strategy:",if_strat)
    print("Enging with Market:",if_market)
    print(len(invest_list))
    print(invest_list)

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
