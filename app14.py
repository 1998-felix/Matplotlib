import matplotlib.pyplot as pt
import numpy as np
import urllib
import matplotlib.dates as mpt

def graph_stocks():
    stock_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_url).read().decode()

    stock_data = []
    source_split = source_code.split("\n")
    for line in source_split:
        split_line = line.split(",")
        if len(split_line)==6:
            if "Date" not in split_line:
                stock_data.append(line)

    Date, Open, High, Low,\
    Close, Adjusted_close,\
    Volume = np.loadtxt(stock_data, delimiter=",",unpack=True,
                        converters={0:bytespdate('%Y-%m-%d')})