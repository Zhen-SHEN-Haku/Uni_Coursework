import yfinance as yf
import pandas as pd


def calculate_returns(s):
    data = yf.download(s, start="2002-1-30", end="2003-1-30")
    returns=(data['Close']/data['Close'].shift(1))-1
    re=returns.resample('M').mean()
    re.dropna(axis=0,how="any")
    return(re)
market_returns = calculate_returns("^GSPC")

def cov(s):
    data = yf.download(s, start="2002-1-30", end="2003-1-30")
    returns = (data['Close'] / data['Close'].shift(1)) - 1
    re = returns.resample('M').mean()
    re.dropna(axis=0, how="any")
    """
    for i, j in re.iterrows():
        j = j.to_frame()  # series有转frame dict等方法
        j = pd.DataFrame(j.values.T, columns=j.index)
    """
    re["market"] = market_returns[1]
    cov_with_market = cov(re[1],market_returns)
    return cov_with_market
cov("AAPL")

"""
# correlation
corr = []
market_var = returns['^GSPC'].var()
market_sd = market_var^(1/2)
for i in range(len(cov_with_market)):
    corr.append(cov_with_market[i]/(market_sd*returns.std()))
"""
