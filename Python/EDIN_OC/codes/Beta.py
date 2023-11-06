from yahoofinancials import YahooFinancials

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

stocks = ['CSCO', 'QCOM', 'AMAT', 'LRCX', 'KLAC', 'LMT', 'TSLA', 'AAPL', 'CI', 'REGN', 'PFE', 'BX', 'HII', 'NVDA', 'SQ', 'AMCR', 'MS']
Beta = []
for i in stocks:
    yahoo_financials = YahooFinancials(i)
    a = yahoo_financials.get_beta()
    print(i)
    Beta.append(a)


