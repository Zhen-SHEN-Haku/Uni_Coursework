import tushare as ts


ts.set_token('98c8afd1da75fd2b3388b7ee4cd7d8597fc428577e6cd596780bbdce')
pro = ts.pro_api()
df = pro.us_basic()