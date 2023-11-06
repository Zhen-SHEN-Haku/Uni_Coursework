from yahoofinancials import YahooFinancials
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def calculate_ROE(s):
    ticker = s
    yahoo_financials = YahooFinancials(ticker)
    income_statement_data_m = yahoo_financials.get_financial_stmts('m', 'balance')
    tA = []
    tL = []
    for i in ticker:
        lst1 = income_statement_data_m['balanceSheetHistoryQuarterly'][i]
        total_assets = []
        total_liability = []
        for j in lst1:
            for k in j.keys():
                k = str(k)
                total_assets.append(j[k]['totalAssets'])
                total_liability.append(j[k]['totalLiab'])
        tA.append(np.mean(total_assets))
        tL.append(np.mean(total_liability))
        income = yahoo_financials.get_net_income()
        nI = []
        ROE = []
        for i in income.keys():
            i = str(i)
            nI.append(income[i])
        for i in range(len(tA)):
            ROE.append(nI[i] / (tA[i] - tL[i]))
        return ROE


ticker = ['AAPL','AMZN']
yahoo_financials = YahooFinancials(ticker)
income_statement_data_m = yahoo_financials.get_financial_stmts('m', 'balance')
tA = []
tL = []
for i in ticker:
    lst1 = income_statement_data_m['balanceSheetHistoryQuarterly'][i]
    total_assets = []
    total_liability = []
    for j in lst1:
        for k in j.keys():
            k = str(k)
            total_assets.append(j[k]['totalAssets'])
            total_liability.append(j[k]['totalLiab'])
    tA.append(np.mean(total_assets))
    tL.append(np.mean(total_liability))
income = yahoo_financials.get_net_income()
nI = []
ROE = []
for i in income.keys():
    i = str(i)
    nI.append(income[i])
for i in range(len(tA)):
    ROE.append(nI[i] / (tA[i] - tL[i]))


