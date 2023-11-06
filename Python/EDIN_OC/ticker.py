import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

ticker = []
with open("name.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        ticker.append(row[0])
a = ['BRK.B', 'PARA', 'CEG', 'BF.B', 'V', 'XOM', 'CVX', 'WMT', 'MRK', 'T', 'UPS', 'BMY', 'NEE', 'CVS', 'ORCL', 'COP', 'BA', 'GE', 'DUK', 'F', 'SO', 'EOG', 'HUM', 'PXD', 'MRNA', 'NXPI', 'MPC', 'DOW', 'SRE', 'HLT', 'DD', 'DLR', 'PSX', 'CTVA', 'VLO', 'OXY', 'DVN', 'AMP', 'WBA', 'PEG', 'EXPE', 'HAL', 'TWTR', 'DAL', 'LUV', 'HES', 'BKR', 'ALB', 'EIX', 'FANG', 'ABC', 'RCL', 'CTRA', 'CCL', 'WDC', 'MRO', 'MGM', 'CZR', 'MOS', 'CF', 'UDR', 'CAH', 'LVS', 'UAL', 'LYV', 'KIM', 'AES', 'HST', 'INCY', 'RE', 'APA', 'AAL', 'NI', 'WYNN', 'AIZ', 'CDAY', 'DXC', 'PBCT', 'FRT', 'NCLH', 'ALK', 'RL']
for i in a:
    ticker.remove(i)
print(ticker)
