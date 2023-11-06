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

