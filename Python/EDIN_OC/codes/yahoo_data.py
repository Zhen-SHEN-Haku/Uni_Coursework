import pandas_datareader.data as web
import datetime


start = datetime.datetime(2019,1,1)
end = datetime.datetime(2021,12,30)

symbol = '603955.SS'
stocks = web.DataReader(symbol, 'yahoo',start,end)

stocks.to_csv('LPE.PA.csv')
