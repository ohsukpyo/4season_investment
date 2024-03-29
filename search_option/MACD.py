import sys
sys.path.append("/Users/josephkim/Desktop/bitcoin_trading_back") 
from BitThumbPrivate import BitThumbPrivate
import pandas as pd
import numpy as np

bit = BitThumbPrivate()

def MACD_condition(coin_list, chart_term, short, long, signal, up_down):
    # print("MACD_condition coin_list :::::", coin_list)
    close_data = []
    date_data = []
    return_coin =[]
    for coin in coin_list:
        item = {"id": str(coin).replace("_KRW", ""), "term": chart_term}
        row_candle_data = bit.calndel_for_search(item)
        candle_data = list(row_candle_data.values())
        for data in candle_data[1]:
            close_data.append(float(data[2]))
            date_data.append(float(data[0]))
        pd_data = pd.DataFrame({'date':date_data,'close':close_data})
        close_price = pd_data['close']
        short_ema = close_price.ewm(span=int(short), adjust=False).mean()
        long_ema = close_price.ewm(span=int(long), adjust=False).mean()
        macd_line = short_ema - long_ema
        signal_line = macd_line.ewm(span=int(signal), adjust=False).mean()
        histogram = macd_line - signal_line
        macd_data = pd.DataFrame({
            'Name': str(coin).replace("_KRW", ""),
            'MACD': macd_line,
            'Signal': signal_line,
            'Histogram': histogram
        })
        
        if up_down == 'up':
            if float(macd_data.iloc[-1]['Signal']) < float(macd_data.iloc[-1]['MACD']): 
                return_coin.append(str(coin).replace("_KRW", ""))
        elif up_down == 'down':
            if float(macd_data.iloc[-1]['Signal']) > float(macd_data.iloc[-1]['MACD']): 
                return_coin.append(str(coin).replace("_KRW", ""))

    print("macd_data return_coin :::: ", return_coin)
    return return_coin
