import sys
sys.path.append("/Users/josephkim/Desktop/bitcoin_trading_back") 
from BitThumbPrivate import BitThumbPrivate
import pandas as pd
import numpy as np

bit = BitThumbPrivate()
def Disparity_condition(coin_list):
    print("Disparity_condition coin_list :::::", coin_list)
    term = 15
    return_value = []
    close_data =[]
    date_data =[]
    for coin in coin_list:
        item = {"id": str(coin).replace("_KRW", ""), "term": "1h"}
        row_candle_data = bit.calndel_for_search(item)
        candle_data = list(row_candle_data.values())
        for data in candle_data[1]:
            close_data.append(float(data[2]))
            date_data.append(float(data[0]))
        pd_data = pd.DataFrame({'date':date_data,'close':close_data})
        close_price = pd_data['close']
        masp_ema = close_price.ewm(span=term, adjust=False).mean()
        arr_close = float(close_price.iloc[-1])
        arr_masp = float(masp_ema.iloc[-1])
        if (arr_masp / arr_close) * 100 > 100: 
            return_value.append(str(coin).replace("_KRW", ""))
            print("Disparity_condition :::: ",str(coin).replace("_KRW", ""), (arr_masp / arr_close) * 100)
    return return_value