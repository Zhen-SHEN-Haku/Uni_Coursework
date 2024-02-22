import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from fredapi import Fred
import datetime
from scipy.stats import normaltest,shapiro,kstest
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.stattools import acf,pacf,adfuller,coint,kpss
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.diagnostic import kstest_normal,lilliefors
from statsmodels.tsa.ar_model import AutoReg

warnings.filterwarnings('ignore')

"""
Not all the results are used in the report; only selected parts are shown.
"""

# Time series
fred = Fred(api_key='71ab4b1f93d478e1b9f1bae203c01972') # access data using api

# 1. download data and adjust the data for plotting
EuroCurrency = fred.get_series('EVZCLS','1/1/2022', '20/2/2024').dropna()[-300:] # EuroCurrency VI, with T = 300 and a daily resolution
Gold = fred.get_series('GVZCLS','1/1/2022', '20/2/2024').dropna()[-300:] # Gold VI, with T = 300 and a daily resolution 
df1 = pd.concat([EuroCurrency,Gold],axis=1) # combine two time series
df1.columns = ['EuroCurrency','Gold'] # rename the column label

# 2. plot figure 
plt.figure()
plt.plot(df1)
plt.gcf().autofmt_xdate() # beauty the x-axis
plt.title('Price time series figure')
plt.ylabel('Price')
plt.legend(['EuroCurrency','Gold'])

# Moving averages
# 3. Define mathematically the moving average of the price time series with an arbitrary time- window τ
# see in the report

# 4. Compute three moving averages
df1_eu, df1_gold = [pd.DataFrame(),pd.DataFrame()] # split the data for subplots
df1_eu['EuroCurrency'], df1_gold['Gold'] = [df1['EuroCurrency'], df1['Gold']] # copy the origin data
# Compute the MAs with different time-windows
df1_eu['EU_MA5'] = df1['EuroCurrency'].rolling(5).mean() 
df1_eu['EU_MA20'] = df1['EuroCurrency'].rolling(20).mean()
df1_eu['EU_MA60'] = df1['EuroCurrency'].rolling(60).mean()
df1_gold['Gold_MA5'] = df1['Gold'].rolling(5).mean()
df1_gold['Gold_MA20'] = df1['Gold'].rolling(20).mean()
df1_gold['Gold_MA60'] = df1['Gold'].rolling(60).mean() 
# print('Moving average data:','\n',df1_eu.tail(),'\n',df1_gold.tail())

# 5. Plot the MA against the price time series
f, (ax1,ax2) = plt.subplots(2,sharex=True)
f.suptitle('The moving averages against the price time series')
ax1.plot(df1_eu) # due to the maximum time-window is 60, plot start from the 61st value
ax1.set_title('EuroCurrency')
ax1.legend(['Origin','MA5','MA20','MA60'],loc=1)
ax2.plot(df1_gold)
ax2.set_title('Gold')
ax2.legend(['Origin','MA5','MA20','MA60'],loc=1)

# 6. Compute the linear and log-return of the price time series
def daily_return(x,type='linear'): # Compute the linear or log return depends on the input
    if type == 'linear':
        return (x.shift(-1)/x - 1).dropna()
    elif type == 'log':
        return (np.log(x.shift(-1)/x)).dropna()
    
linear_r = daily_return(df1[['EuroCurrency','Gold']]) # linear return
log_r = daily_return(df1[['EuroCurrency','Gold']],type='log') # log-return 

df2 = pd.concat([linear_r['EuroCurrency'],log_r['EuroCurrency']],axis=1) # returns for EuroCurrency
df2.columns = ['Linear','Log']
df3 = pd.concat([linear_r['Gold'],log_r['Gold']],axis=1) # returns for Gold
df3.columns = ['Linear','Log']
# print('EuroCurrency return:','\n',df2.tail(),'\n'+'Gold return:','\n',df3.tail())

# 7.Plot the linear return against the log-return time series
fig, (ax1,ax2) = plt.subplots(2,sharex=True)
fig.suptitle('The plot of linear return against the log-return time series')
ax1.plot(df2)
ax1.set_title('EuroCurrency')
ax1.legend(['Linear_EuroCurrency','Log_EuroCurrenct'], loc = 1)
ax2.plot(df3)
ax2.set_title('Gold')
ax2.legend(['Linear-Gold','Log_Gold'], loc = 1)

# Time Series Analysis
# 8. Define the auto-correlation function (for a stationary time-series)
# see in the report

# 9. Compute the auto-correlation functions (ACF) of the price time series
auto_eu,auto_gold = [acf(df1['EuroCurrency'],nlags=300),acf(df1['Gold'],nlags=300)]
def compute(x,y,str): # print the result of computation
    df = pd.DataFrame({'EuroCurrency':x,'Gold':y})
    # print (str,'\n',df.tail())
compute(auto_eu,auto_gold,'ACF data of the price time series:')

# 10. Plot the price ACFs
def acff(x,category): # plot acf figure using computed data
    plt.figure() 
    plt.plot(x)
    plt.title('The auto-correlation function of '+ category)
    plt.xlabel('Lag')
    plt.ylabel('Auto-correlation')

acff(auto_eu,'EuroCurrency')
acff(auto_gold,'Gold')

def acf_direct(df,str,type): # plot using autocorrelation_plot, without using computed data
    if type == 1:
        plot_acf(df)
        plt.title(str)
    if type == 2:
        plt.figure()
        autocorrelation_plot(df)
        plt.title(str)

acf_direct(df1['EuroCurrency'],'The auto-correlation function of EuroCurrency',1)
acf_direct(df1['Gold'],'The auto-correlation function of Gold',1)

# 11. Compute the partial auto-correlation functions (PACF) of the price time series
pacf_eu,pacf_gold = [pacf(df1['EuroCurrency'],method='ywm'),pacf(df1['Gold'],method='ywm')]
compute(pacf_eu,pacf_gold,'PACF data of the price time series:')

# 12. Plot the price PACFs
def pacff(x,str): # plot pacf figure using computed data
    plt.figure()
    plt.scatter([range(1,26)],x)
    plt.vlines([range(1,26)], 0, x, colors='b', lw=1, alpha=0.2)
    plt.title('The partial auto-correlation functions of ' + str)
    plt.xlabel('Lag')
    plt.ylabel('PACF')

pacff(pacf_eu,'EuroCurrency')
pacff(pacf_gold,'Gold')

def pacf_direct(df,str): # plot pacf figure directly, without using the computed data
    plot_pacf(df)
    plt.title(str)
    plt.xlabel('Lag')
    plt.ylabel('PACF')

pacf_direct(df1['EuroCurrency'],'The partial auto-correlation functions of EuroCurrency')
pacf_direct(df1['Gold'],'The partial auto-correlation functions of Gold')

# 13. Compute the auto-correlation function (ACF) of the return time series
acf_eur,acf_gr = [acf(linear_r['EuroCurrency'],nlags=299),acf(linear_r['Gold'],nlags=299)]
compute(acf_eur,acf_gr,'ACF data of the return time series:')

# 14. Plot the return ACFs
acff(acf_eur,'EuroCurrency return')
acff(acf_gr,'Gold return')
acf_direct(linear_r['EuroCurrency'],'The auto-correlation function of EuroCurrency return',2)
acf_direct(linear_r['Gold'],'The auto-correlation function of Gold return',2)

# 15. Compute the partial auto-correlation functions (PACF) of the return time series
pacf_eur,pacf_goldr = [pacf(linear_r['EuroCurrency'],method='ywm'),pacf(linear_r['Gold'],method='ywm')]
compute(pacf_eur,pacf_goldr,'PACF data of the return time series:')

# 16. Plot the return PACFs
pacff(pacf_eur,'EuroCurrency return')
pacff(pacf_goldr,'Gold return')

pacf_direct(linear_r['EuroCurrency'],'The partial auto-correlation functions of EuroCurrency return')
pacf_direct(linear_r['Gold'],'The partial auto-correlation functions of Gold return')

# Gaussianity and Stationarity test
# 17. Introduce mathematically a Gaussianity test
# see in the report 

# 18. Perform a Gaussianity test of the return time series
# normaltest(linear_r['EuroCurrency'])
# normaltest(linear_r['Gold'])

# test using Kolmogorov-Smirnov Distribution Test
# stat,p1 = kstest_normal(linear_r['EuroCurrency'],'norm')
# stat,p2 = kstest_normal(linear_r['Gold'],'norm')   

# test using Shapiro-Wilk test
stat,p1 = shapiro(linear_r['EuroCurrency'])
stat,p2 = shapiro(linear_r['Gold'])   
print('The pvalue for Shapiro-Wilk test of linear returns:'+'\n'+'EuroCurrency:',p1,'\n'+'Gold:',p2)

# quite small pvalue
# f,(ax1,ax2) = plt.subplots(2,sharex=True,figsize = [6.4,6.4])
# qqplot(linear_r['EuroCurrency'],line='45',ax=ax1)
# qqplot(linear_r['Gold'],line='45',ax=ax2)
# ax1.set_title('qqplot for EuroCurrency')
# ax2.set_title('qqplot for Gold')
qqplot(linear_r['EuroCurrency'],line='s')
qqplot(linear_r['Gold'],line='s')
# 19. Introduce mathematically a stationarity test
# see in the report

# 20. Perform a stationarity test of the return time series
# def adf_test(df):
#     x = adfuller(df, autolag='AIC')
#     return print('The adf test statistic is',x[0],', pvalue is',x[1])

# adf_test(linear_r['EuroCurrency'])
# adf_test(linear_r['Gold'])
print(adfuller(linear_r['EuroCurrency']))
print(adfuller(linear_r['Gold']))

print(kpss(linear_r['EuroCurrency']))
print(kpss(linear_r['Gold']))

# print(adfuller(df1['EuroCurrency']))
# print(adfuller(df1['Gold']))



# Conintegration
# 21. Define mathematically a cointegration test
# see in the report

# 22. Perform a cointegration test of the two ETF price time series
def cointegrated(x,y,str): 
    score, pvalue, _ = coint(x,y)
    return print('The conintegrated test pvalue of '+ str +' is' , pvalue)
cointegrated(df1['EuroCurrency'],df1['Gold'],'the two ETF price time series')
# print(coint(df1['EuroCurrency'],df1['Gold']))
print(adfuller(df1['EuroCurrency']))
print(adfuller(df1['Gold']))
print(adfuller(np.diff(df1['EuroCurrency'])))
print(adfuller(np.diff(df1['Gold'])))

# 23. Perform a cointegration test of the two ETF return time series

# cointegrated(linear_r['EuroCurrency'],linear_r['Gold'],'the two ETF linear return time series')
# cointegrated(log_r['EuroCurrency'],log_r['Gold'],'the two ETF log-return time series')
# print(coint(linear_r['EuroCurrency'],linear_r['Gold']))
# print(coint(log_r['EuroCurrency'],log_r['Gold']))
print(coint(df1['EuroCurrency'],df1['Gold']))

plt.show()

# find the coefficients
# ar_model = AutoReg(df1['Gold'], lags = 2).fit()
# ar_model.summary()

