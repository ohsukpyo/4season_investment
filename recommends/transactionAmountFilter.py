import pandas as pd

# 거래대금 데이터, 범위 받아 조건에 맞는 코인 리턴 (수집기 수정후 수집기데이터 사용으로 수정예정)
def transactioAmountRecommend(nowstamp, coinList, dfList, chart_term, lowTransactionAmount, highTransactionAmount):
    print('-----------------------------------------------------------------------------------------------------------')
    print('transactio amount start ::::::: ')
    print('before condition pass coins ::::::: ', len(coinList))

    transactionAmount_list = []
    transactionAmount_value = []
    time = nowstamp - ((int(chart_term[:-1]) + 1) * 60) if chart_term[-1] == 'm' else nowstamp - ((int(chart_term[:-1]) + 1) * 3600)

    df = pd.DataFrame(dfList)
    time_satisfied_df = df.loc[df['S_time'] > time]

    for coin in coinList:
        if coin in coinList:
            matching_coin_name_df = time_satisfied_df.loc[df['coin_name'] == coin]
            if len(matching_coin_name_df) != 0 and matching_coin_name_df['Transaction_amount'].sum() > float(lowTransactionAmount) and matching_coin_name_df['Transaction_amount'].sum() < float(highTransactionAmount):
                transactionAmount_list.append(coin)
                transactionAmount_value.append({'coin_name': coin, 'Transaction_amount': matching_coin_name_df['Transaction_amount'].sum()})

        else:
            pass

    print('transactio amount end ::::::: ', len(transactionAmount_list))
    print('-----------------------------------------------------------------------------------------------------------')
    return transactionAmount_list, transactionAmount_value