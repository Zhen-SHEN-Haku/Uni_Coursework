"""
stocktrader -- A Python module for virtual stock trading
This module can load the historical data of the stocks and do automatic trading depending on some parameters which can
achieving in a bit more than six years multiplied initial investment by a factor of almost seven.
It can simulate simple stocks trading depend on historical data.
Full name: ZHEN SHEN
StudentId: 10725458
Email: zhen.shen-4@student.manchester.ac.uk
"""
import csv
import os
import re
import pandas as pd

class TransactionError(Exception):
    pass
class DateError(Exception):
    pass

stocks = {}  # {symbol,{date:YYYY-MM-DD:[Open,High,Low,Close]}}
portfolio = {}  # {date:xx,cash:xx,symbol:xx}
transactions = []  # a list of dicts, list = [{date:xx,symbol:xx,volume:xx}]
def normaliseDate(s):
    """
    Input as YYYY-MM-DD,YYYY/MM/DD or DD.MM.YYYY
    Return as YYYY-MM-DD
    DateError for wrong patterns other than these three patterns.
    """
    date_list = [] # Separate storage of year, month and day data.
    pattern1 = '^\d{4}\-\d{1,2}\-\d{1,2}$' # YYYY-MM-DD
    pattern2 = '^\d{1,2}\.\d{1,2}\.\d{4}$'# DD-MM-YYYY
    pattern3 = '^\d{4}\/\d{1,2}\/\d{1,2}$'# YYYY\MM\DD
    # use 3 patterns to avoid pattern like YYYY-MM/DD which should cause an error
    if re.match(pattern1, s) is not None or re.match(pattern2, s) is not None or re.match(pattern3, s) is not None:
        if '-' in s: # split by '-' '/' '.'
            date_list = s.split('-')
        if '/' in s:
            date_list = s.split('/')
        if '.' in s:
            date_list = s.split('.')
            a = date_list[2]
            date_list[2] = date_list[0]
            date_list[0] = a # rearrange the order into YYYY,MM,DD
        if len(date_list[1]) == 1:
            date_list[1] = ('0' + date_list[1]) # add a '0' if there is only a number for month or day
        if len(date_list[2]) == 1:
            date_list[2] = ('0' + date_list[2]) # add a '0' if there is only a number for month or day
        return ''.join((date_list[0], '-', date_list[1], '-', date_list[2])) # combine them as the requirement
    else:
        raise DateError

def loadStock(symbol):
    """
    Input stocks' symbols and return nothing while load corresponding historical data in stocks dictionary.
    FileNotFoundError for file not found, ValueError for an invalid format.
    """
    fname = symbol + '.csv'
    if not os.path.exists(fname): # found the file if it exists.
        raise FileNotFoundError # raise the error if the file can not be found
    with open(fname) as f:
        reader = csv.reader(f)
        date = [row[0] for row in reader] # read the data of csv files into a list
        del date[0] # delete the first row which is the header[date,open,high,low,close]
        for i in range(len(date)):
            try:
                date[i] = normaliseDate(date[i]) # try whether the format of the date is correct
            except DateError:
                raise ValueError
        # as the requirement in this function, when normaliseDate function raise DateError, it should raise ValueError
    value = pd.read_csv(fname, usecols=[1, 2, 3, 4], skiprows=0)
    # skip the row of headers and only read the first four rows
    value = value.values.tolist() # changing data type to list
    for i in value:
        for j in i:
            if type(j) != float: # judge if the data type is float number or not
                raise ValueError
    dicti = {}
    for i in range(len(date)):
        dicti[date[i]] = list(value[i])
    stocks[symbol] = dicti
    return

def loadPortfolio(fname = 'portfolio.csv'):
    """
    Loads the data from the file(input the file name) and assigns them to the portfolio dictionary
    Depending on the shares owned, load stock data into stocks dictionary.
    Return nothing and FileNotFoundError for file not found, ValueError for an invalid format.
    """
    portfolio.clear()
    transactions.clear()
    if not os.path.exists(fname): # found the file if it exists.
        raise FileNotFoundError
    data = []
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row) # read the file row by row
    try:
        datevalue = normaliseDate(str(data[0][0]))
    except DateError:
        # as the requirement in this function, when normaliseDate function raise DateError, it should raise ValueError
        raise ValueError
    cashvalue = 0
    try:
        cashvalue = float(data[1][0])
    except cashvalue < 0 : # when the value of the cash is impossible raise ValueError
        raise ValueError
    key = ['date', 'cash']
    value = [datevalue, cashvalue]
    for i in data:
        if len(i) == 2: # len = 2 means exists format like 'symbol' and 'volume', extraction them for further uses
            key.append(i[0])
            try:
                loadStock(i[0])
            except FileNotFoundError:
                # FileNotFoundError means such symbol does not exists and need to raise a ValueError
                raise ValueError
            value.append(int(i[1]))
    for i in range(len(key)): # combine the list of keys and values into a dictionary
        portfolio[key[i]] = value[i]
    return

def valuatePortfolio(date = None, verbose = False):
    """
    With input date and verbose to valuate the portfolio at a given date and returns a floating point number,
    when verbose = True, print an extra table to show the situation of portfolio.
    DateError for input date is earlier than the date of the portfolio or input date is not a trading day.
    """
    if date is None:
        date = portfolio['date']
    else:
        date0 = portfolio['date']  # date for portfolio
        date = normaliseDate(date)  # date for input( which should be later)
        if date0 > date: # determine if the date matches the requirement
            raise DateError
    cash = portfolio['cash']
    symbol = list(portfolio.keys())[2:] # valuate the value of shares skip the row of date and cash
    volume = list(portfolio.values())[2:] # volumes corresponding to the stocks in order
    low = [] # for insurance purpose, we should calculate the value based on the lowest price
    for company in symbol:
        a = date in stocks[company].keys()
        if not a: # date can not be found in stocks dictionary
            raise DateError
        else:
            low.append(stocks[company][date][2])
    portfolio_value = [{'capital type': 'Cash', 'Volume': 1, 'val/unit': cash, 'value in pounds': cash}]
    for i in range(len(symbol)):
        dict = {'capital type': 'Shares of ' + symbol[i], 'Volume': volume[i], 'val/unit': low[i],
                'value in pounds': low[i] * volume[i]} # dictionary for table printing
        portfolio_value.append(dict)
    total = cash # should not forget the value of cash, add it as the initial value
    for i in range(len(volume)):
        total = total + volume[i] * low[i] # cash + stocks(one by one)
    if verbose is False:
        return total
    if verbose is True: # print the table
        print("Your portfolio on", date, ':\n', '[* share values based on the lowest price on', date + ']\n')
        print("{0:<22} | {1} | {2} | {3:^8} ".format("Capital type", "Volume", "Val/Unit*", "Value in £*"))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + '+' + '-' * 13)
        for capital in portfolio_value:
            print("{capital type:<22} | {Volume:6.0f} | {val/unit:9.2f} | {value in pounds:>12.2f}".format(**capital))
        print("-" * 23 + "+" + "-" * 8 + "+" + "-" * 11 + '+' + '-' * 13)
        print("TOTAL VALUE                                      {:.2f}\n".format(total))
        return total
    return

def addTransaction(trans, verbose = False):
    """
    Input with a trans dictionary and verbose,
    update the information in portfolio dictionary while none error raised.
    Print a message about the portfolio after transaction if verbose = True.
    DateError for input date is earlier than the date of the portfolio.
    ValueError for the transaction is not listed in the stocks dictionary
    or the volume or cash is not enough to continue a transaction.
    """
    date0 = portfolio['date']  # date for portfolio
    date = normaliseDate(trans['date']) # date for input( which should be later)
    if date0 > date:
        raise DateError
    symbol = trans['symbol']
    volume = trans['volume']
    a = date in stocks[symbol].keys()
    if a is False: # date can not be found in stocks dictionary
        raise ValueError
    else:
        low = stocks[symbol][date][2] # low price
        high = stocks[symbol][date][1] # high price
    if volume > 0: # buying transaction
        try: # use try to avoid data change which may caused by a wrong transaction
            portfolio['cash'] = portfolio['cash'] - abs(volume) * high # whether cash is enough or not
        except portfolio['cash'] < 0:
            raise TransactionError
    elif volume < 0: # selling transaction
        try:
            portfolio['cash'] = portfolio['cash'] + abs(volume) * low
        except volume > portfolio[symbol]: # whether the volume of stocks is enough or not
            raise TransactionError
    if symbol in list(portfolio.keys()):
        portfolio[symbol] = portfolio[symbol] + volume
    else:
        portfolio[symbol] = volume # for stocks not in portfolio before,, add it in portfolio dictionary
    if portfolio[symbol] == 0:
        # delete the key-value while the volume is 0 which means we don't have the stock for this company
        del portfolio[symbol]
    portfolio['date'] = date
    transactions.append(trans) # make sure the transaction could be trading, add it into the trans list
    if verbose is True:
        if volume < 0: # print for sell trading
            print(date + ': Sold', '{:.0f}'.format(abs(volume)), 'shares of', symbol,'for a total of £' + '{:.2f}'.format(abs(volume) * low),'\n' + 'Available cash: £' + '{:.2f}'.format(portfolio['cash']))
        elif volume > 0: # print for buy trading
            print(date + ': Bought', '{:.0f}'.format(abs(volume)), 'shares of', symbol,'for a total of £' + '{:.2f}'.format(abs(volume) * high),'\n' + 'Remaining cash: £' + '{:.2f}'.format(portfolio['cash']))
    return

def savePortfolio(fname = 'portfolio.csv'):
    """
    Saves the current dictionary portfolio to a CSV file with name fname and return nothing.
    """
    with open(fname, 'w') as f:
        w = csv.writer(f)
        w.writerows(portfolio.items())
    return

def sellAll(date = None, verbose = False):
    """
    Sells all shares in the portfolio on a particular date. Print all selling transactions while verbose  = True.
    """
    if date is None:
        date = portfolio['date']
    else:
        date = normaliseDate(date)
    if len(portfolio) >= 3: # len >= 3 which means has stocks (except 'date' and 'cash')
        keys = list(portfolio.keys())
        del keys[:2] # skip the 'date' and 'cash' items
        for i in keys:
            trans = {'date' : date, 'symbol' : i, 'volume' : -portfolio[i]}
            # use '-portfolio[i]' to achieve sell all shares which equal to the volume in portfolio
            addTransaction(trans,verbose)
    return

def loadAllStocks():
    """
    Loads all stocks into the dictionary stocks and return nothing.
    Ignored the file if it fails.
    """
    list1 = os.listdir(os.path.dirname(os.path.abspath('stocktrader.py')))
    file_name = []
    for i in list1:
        if re.match('^[A-Z]+\.csv$',i) is not None:
            # selecting the name of the files which should be 'XYZ(any number of capital letters).csv'
            file_name.append(re.sub('.csv','',i)) # in order to use loadStock function, remove the '.csv' in file name
    for i in file_name:
        try:
            loadStock(i)
        except ValueError: # skip the fail files
            pass
    return

def tradeStrategy1(verbose = False):
    """
    Goes through all trading days in the dictionary stocks and trading shares automatically
    depend on two parameters Q_buy and Q_sell.
    Assume sell at daily lowest price and buy at daily highest price.
    Print all the transactions while verbose = True.
    """
    lst = list(stocks[list(stocks.keys())[0]].keys()) # the list of trading dates
    slst = list(stocks.keys()) # the list of companies' symbols
    j = lst.index(max(portfolio['date'], lst[9]))
    # The earliest buying decision isthe date of the portfolio or the 10th available trading day (whichever is later)
    def H(s, j): # the high price on the given index of the day for the given stock
        return stocks[s][lst[j]][1]
    def L(s, k): # the low price on the given index of the day for the given stock
        return stocks[s][lst[k]][2]
    def Q_buy(s, j): # the parameter for making buying decisions
        sum = 0
        for i in range(0,10):
            sum = sum + H(s,j-i)
        return 10 * H(s, j) / sum
    def Q_sell(s, j, k): # the parameter for making selling decisions
        return L(s, k) / H(s, j)
    while j in range(0, len(lst)):
        q_max = 0
        for s in slst:
            if Q_buy(s, j) > q_max: # choose the greatest one to buy
                q_max = Q_buy(s, j)
                symbol = s
        trans = {'date': lst[j], 'symbol': symbol, 'volume': portfolio['cash'] // H(symbol, j)} # add a new transaction
        addTransaction(trans, verbose)
        for k in range(j + 1, len(lst)): # the situation that we should sell the stocks
            if Q_sell(symbol, j, k) < 0.7 or Q_sell(symbol, j, k) > 1.3:
                trans = {'date': lst[k], 'symbol': symbol, 'volume': -portfolio[symbol]} # add a new transaction
                break
            else:
                trans['volume'] = 0
                # avoid do the last transaction twice
        addTransaction(trans, verbose)
        j = k + 1 # j be the day after transactions
    return

def main(): # Test your functions here
    return
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    main()
