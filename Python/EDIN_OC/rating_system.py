
def score_stocks(stock_dict):
    #评分系统
    f = list(zip(stock_dict.keys(), stock_dict.values()))
    rating = {}
    for i in list(stock_dict.keys()):
        f.sort(key=lambda x: x[1], reverse=False)
