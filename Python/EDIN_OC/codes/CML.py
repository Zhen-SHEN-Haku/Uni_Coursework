import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pylab import mpl
from datetime import date
import pandas_datareader.data as web
import pandas as pd
import numpy as np
from scipy import optimize
"""
def calculate_risks(s):
    data = yf.download(s, start="2002-1-30", end="2021-1-30")
    returns=(data['Close']/data['Close'].shift(1))-1
    re=returns.resample('M').std().dropna(axis=0,how="any")
    return(re)
calculate_risks("^GSPC  ^IXIC  ^GDAXI  ZF=F")

def calculate_EXCEED_returns(s):
    tr=calculate_returns(s)
    rf=calculate_returns("^TNX")
    risk_pri=tr-rf
    return(risk_pri)
calculate_EXCEED_return("AAPL")

BETA={}
def Beta_regression(portfolio,verbose=None):
    X=calculate_EXCEED_returns("^GSPC") #计算 Excess！！
    Y=calculate_EXCEED_returns(portfolio)
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    beta = numer / denum
    alpha = ybar - beta * xbar
    yfit = [alpha + beta * xi for xi in X]
    BETA[portfolio]=beta
    if verbose is True:
        plt.plot(X, yfit,'-r',label=portfolio)
        plt.scatter(X,Y)
        plt.axis([-0.03,0.04,-0.03,0.04])
        plt.xlabel("Volatility(standard deviation)")
        plt.ylabel("Expected Return")
        plt.legend()
        print()
    return
"""

def RF():
    N_DAYS = 90
    df_rf = yf.download('^TNX', start="2016-1-30", end="2022-1-30")
    rf = df_rf.resample('M').last().Close / 100
    rf = (1 / (1 - rf * N_DAYS / 360)) ** (1 / N_DAYS)
    rf = (rf ** 30) - 1
    rf.plot(title='Risk-free rate')
    return plt.show()
RF()



def CML():
    # risk free rate
    rf = 0.002

    # r
    Mkt = yf.download('^GSPC', start="2019-1-30", end="2021-1-30")
    Mkt = Mkt.resample('M').last().Close / 100
    Rf = yf.download('^TNX', start="2019-1-30", end="2021-1-30")
    Rf = Rf.resample('M').last().Close/100

    data = pd.concat([df],axis=1)
    data.columns = ['S&P500','^TNX']
