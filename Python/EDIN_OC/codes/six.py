import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
tech = []
with open("tech.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        tech.append(row[0])
health = []
with open("health.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        health.append(row[0])
finance = []
with open("finance.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        finance.append(row[0])
energy = []
with open("energy.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        energy.append(row[0])
industry = []
with open("industry.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        industry.append(row[0])
raw = []
with open("raw.csv")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        raw.append(row[0])

QEG = ['ABBV', 'DIS', 'BXP', 'HPE', 'LYB', 'NLSN', 'NUE', 'REG', 'IT', 'TSLA', 'FIS', 'WTW', 'GILD', 'DRE', 'ANTM', 'NRG', 'NDSN', 'O', 'AIG', 'NWSA', 'NWS', 'PFE', 'PTC', 'RTX', 'NLOK', 'NOW', 'VTR', 'EQR', 'SPG']
PEG = ['PFE', 'CTRA', 'LYB', 'BKR', 'WFC', 'COF', 'DOW', 'DFS', 'NUE', 'EOG', 'F', 'TJX', 'SYF', 'PXD', 'FANG', 'MAR', 'HLT', 'ROST', 'BKNG', 'LEN', 'RF', 'ULTA', 'HAL', 'DAL', 'AIG', 'MU', 'OXY']
PE = ['FB', 'HD', 'BAC', 'PFE', 'CSCO', 'WFC', 'VZ', 'CMCSA', 'QCOM', 'PM', 'LOW', 'MS', 'AMAT', 'AXP', 'IBM', 'ANTM', 'BLK', 'DE', 'CAT', 'MU', 'TGT', 'LMT', 'CB', 'MMM', 'PNC', 'TFC', 'LRCX', 'CSX', 'USB', 'GILD', 'CI', 'ICE', 'D', 'FCX', 'PGR', 'HCA', 'KLAC', 'EMR', 'FDX', 'GD', 'TEL', 'SPG', 'DG', 'BK', 'ADM', 'AEP', 'TRV', 'GIS', 'AZO', 'SIVB', 'STT', 'FITB', 'ROST', 'TROW', 'PCAR', 'CMI', 'WY', 'OKE', 'TSN', 'SWK', 'NTRS', 'HIG', 'MTB', 'HBAN', 'URI', 'FTV', 'CFG', 'SWKS', 'PKI', 'FE', 'STX', 'ETR', 'RJF', 'VFC', 'DRI', 'PFG', 'AMCR', 'OMC', 'EXPD', 'KMX', 'CAG', 'GRMN', 'CNP', 'NVR', 'K', 'NLOK', 'AVY', 'SJM', 'QRVO', 'AAP', 'PKG', 'EVRG', 'FOXA', 'CMA', 'LKQ', 'LDOS', 'IRM', 'WRB', 'WRK', 'FBHS', 'CHRW', 'HSIC', 'SNA', 'TPR', 'BWA', 'UHS', 'NWL', 'GL', 'PNR', 'CPB', 'DISCK', 'DVA', 'PNW', 'HII', 'PVH', 'FOX', 'DISCA', 'UAA', 'UA']
EPS = ['NVR', 'BIO', 'GOOG', 'GOOGL', 'AZO', 'AMZN', 'REGN', 'GS', 'COO', 'MHK', 'BLK', 'SIVB', 'MTD', 'WHR', 'LRCX', 'ORLY', 'NOC', 'LH', 'COF', 'CMG', 'CE', 'CI', 'ANTM', 'CHTR', 'LMT', 'TMO', 'HUM', 'CB', 'HCA']
set1 = set(QEG)
set2 = set(PEG)
set3 = set(PE)
set4 = set(EPS)
seta = set(tech)
setb = set(health)
setc = set(finance)
setd = set(energy)
sete = set(industry)
setf = set(raw)
a = set1.union(set2).union(set3).union(set4)
techi = list(seta.intersection(a))
healthi = list(setb.intersection(a))
financei = list(setc.intersection(a))
energyi = list(setd.intersection(a))
industryi = list(sete.intersection(a))
rawi = list(setf.intersection(a))