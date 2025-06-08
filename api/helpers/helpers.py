import pandas as pd
from pandas import DataFrame as df
# import os
# os.environ["MPLCONFIGDIR"] = r"api/tmp"
# import matplotlib.pyplot as plt
# plt.switch_backend('agg')
import requests

# https://twelvedata.com/account
key = "447c9a96d50c47dcb61e7f07ba44e549"
base_url = "https://api.twelvedata.com"
symbol = "UBER"

# Time Series
def get_timeseries(symbol):
    # plt.clf()
    interval = "1week"
    endpoint = '/time_series'
    url = base_url + endpoint
    params = {  
                'apikey': key, 
                'symbol': symbol, 
                'interval': interval,
                'format': 'json'
                }

    r = requests.get(url, params=params)
    rj = r.json()
    data = df(rj['values'])
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['high'] = pd.to_numeric(data['high'])
    meta = df([(rj['meta'])])

    # plt.plot(data['datetime'], data['high'])
    # plt.xlabel("Time")
    # plt.ylabel("$_High")
    # plt.title(f"Chart for {symbol}")
    # fig_save = r"api\static\assets\images\ml\stock\{}.jpg".format(symbol)
    # plt.savefig(fig_save)
    # fig_dir = f'/api/static/assets/images/ml/stock/{symbol}.jpg'
    # print(fig_dir)
    # return fig_dir, meta
    return meta
