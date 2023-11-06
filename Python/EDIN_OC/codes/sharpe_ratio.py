import numpy as np
import math
import random
import csv
import pandas as pd
import pandas_datareader.data as web
import pandas
import statsmodels
import datetime
import matplotlib

start = datetime.datetime(2002,1,29)
end = datetime.datetime(2022,1,28)

tickers = ['^GSPC','PG','NQ=F','EI','BUD','BP'] # targets
data = pd.DataFrame()
for i in tickers:
    data[i] = web.DataReader(i, 'yahoo',start,end)['Close']
sec_returns = (data/data.shift(1))-1

"""
beta value
"""
cov = sec_returns.cov()
cov_with_market = []
beta = []
corr = []
market_var = sec_returns['^GSPC'].var()
market_sd = math.sqrt(market_var)
for i in range(1,sec_returns.shape[1]):# 日收益的covariance
    cov_with_market.append(cov.iloc[0,i])
for i in range(len(cov_with_market)): #correlation
    corr.append(cov_with_market[i]/(market_sd*sec_returns.std()))
for i in range(len(cov_with_market)):
    beta.append(cov_with_market[i]/market_var)


"""
risk free return
"""
RF = pd.read_csv('^TNX.csv', usecols=[5],skipfooter=1,engine='python')
RF = RF.values.tolist()
total = 0
for i in RF:
    total += i[0]
averageRF = total/len(RF)

"""
risk premium
"""
# expected return of market portfolio
MRF = pd.read_csv('^GSPC.csv', usecols=[5],skipfooter=1,engine='python')
MRF = MRF.values.tolist()
total = 0
for i in MRF:
    total += i[0]
averageMRF = total/len(MRF)
MRP = averageMRF - averageRF
RP = []
for i in beta:
    RP.append(0.025 + i * MRP)

"""
sharpe ratio
"""
sd = []
for i in range(1,len(tickers)):
    sd.append(np.std(data[tickers[i]], ddof=1))

sharpe = []
for i in range(len(RP)):
    sharpe.append((RP[i] - averageRF)/sd[i])

#sharpe最大时，对应的股票代码
select = tickers[sharpe.index(max(sharpe))+1]
print(select)


