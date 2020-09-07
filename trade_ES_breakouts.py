# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

import os
import time
from datetime import datetime, timedelta
import itertools
import os
import pickle
import math
from sklearn.preprocessing import StandardScaler
import nest_asyncio
from ib_insync import *
import talib as ta
from talib import MA_Type
nest_asyncio.apply()
ib = IB()
ib.disconnect()
ib.connect('127.0.0.1', 7497, clientId=np.random.randint(10, 1000))
util.startLoop()


class get_data:

    def next_exp_weekday(self):
        weekdays = {2: [5, 6, 0], 4: [0, 1, 2], 0: [3, 4]}
        today = datetime.today().weekday()
        for exp, day in weekdays.items():
            if today in day:
                return exp

    def next_weekday(self, d, weekday):

        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        date_to_return = d + timedelta(days_ahead)  # 0 = Monday, 1=Tuself.ESday, 2=Wednself.ESday...
        return date_to_return.strftime('%Y%m%d')

    def get_strikes_and_expiration(self):
        ES = Future(symbol='ES', lastTradeDateOrContractMonth='20200918', exchange='GLOBEX',
                                currency='USD')
        ib.qualifyContracts(ES)
        expiration = self.next_weekday(datetime.today(), self.next_exp_weekday())
        chains = ib.reqSecDefOptParams(underlyingSymbol='ES', futFopExchange='GLOBEX', underlyingSecType='FUT',underlyingConId=ES.conId)
        chain = util.df(chains)
        strikes = chain[chain['expirations'].astype(str).str.contains(expiration)].loc[:, 'strikes'].values[0]
        [ESValue] = ib.reqTickers(ES)
        ES_price= ESValue.marketPrice()
        strikes = [strike for strike in strikes
                if strike % 5 == 0
                and ES_price - 10 < strike < ES_price + 10]
        return strikes,expiration

    def get_contract(self, right, net_liquidation):
        strikes, expiration=self.get_strikes_and_expiration()
        for strike in strikes:
            contract=FuturesOption(symbol='ES', lastTradeDateOrContractMonth=expiration,
                                                strike=strike,right=right,exchange='GLOBEX')
            ib.qualifyContracts(contract)
            price = ib.reqMktData(contract,"",False,False)
            if float(price.last)*50 >=net_liquidation:
                continue
            else:
                return contract

    def res_sup(self,ES_df):
        ES_df = ES_df.reset_index(drop=True)
        ressupDF = ressup(ES_df, len(ES_df))
        res = ressupDF['Resistance'].values
        sup = ressupDF['Support'].values
        return res, sup

    def ES(self):
        ES = Future(symbol='ES', lastTradeDateOrContractMonth='20200918', exchange='GLOBEX',
                                currency='USD')
        ib.qualifyContracts(ES)
        ES_df = ib.reqHistoricalData(contract=ES, endDateTime=endDateTime, durationStr=No_days,
                                     barSizeSetting=interval, whatToShow = 'TRADES', useRTH = False)
        ES_df = util.df(ES_df)
        ES_df.set_index('date',inplace=True)
        ES_df['RSI'] = ta.RSI(ES_df['close'])
        ES_df['macd'],ES_df['macdsignal'],ES_df['macdhist'] = ta.MACD(ES_df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
        ES_df['MA_9']=ta.MA(ES_df['close'], timeperiod=9)
        ES_df['MA_21']=ta.MA(ES_df['close'], timeperiod=21)
        ES_df['MA_200']=ta.MA(ES_df['close'], timeperiod=200)
        ES_df['EMA_9']=ta.EMA(ES_df['close'], timeperiod=9)
        ES_df['EMA_21']=ta.EMA(ES_df['close'], timeperiod=21)
        ES_df['EMA_50']=ta.EMA(ES_df['close'], timeperiod=50)
        ES_df['EMA_200']=ta.EMA(ES_df['close'], timeperiod=200)
        ES_df['ATR']=ta.ATR(ES_df['high'],ES_df['low'], ES_df['close'])
        ES_df['roll_max_cp']=ES_df['high'].rolling(20).max()
        ES_df['roll_min_cp']=ES_df['low'].rolling(20).min()
        ES_df['roll_max_vol']=ES_df['volume'].rolling(20).max()
        ES_df['EMA_21-EMA_9']=ES_df['EMA_21']-ES_df['EMA_9']
        ES_df['EMA_200-EMA_50']=ES_df['EMA_200']-ES_df['EMA_50']
        ES_df['B_upper'], ES_df['B_middle'], ES_df['B_lower'] = ta.BBANDS(ES_df['close'], matype=MA_Type.T3)
        ES_df.dropna(inplace = True)
        
        return ES_df

    def option_history(self, contract):
        ib.qualifyContracts(contract)
        df = pd.DataFrame(util.df(ib.reqHistoricalData(contract=contract, endDateTime=endDateTime, durationStr=No_days,
                                      barSizeSetting=interval, whatToShow = 'MIDPOINT', useRTH = False, keepUpToDate=False))[['date','close']])
        df.columns=['date',f"{contract.symbol}_{contract.right}_close"]
        df.set_index('date',inplace=True)
        return df

    def options(self, df1,df2):
        return pd.merge(df1,df2, on='date', how='outer').dropna()
stock_owned = np.zeros(2)


ES = Future(symbol='ES', lastTradeDateOrContractMonth='20200918', exchange='GLOBEX',
            currency='USD')
ib.qualifyContracts(ES)
endDateTime = ''
No_days = '2 D'
interval = '1 min'
res = get_data()


    
def flatten_position(contract):
    positions = ib.positions()
    for each in positions:
        if each.contract.right != contract.right:
            continue
        ib.qualifyContracts(each.contract)
        if each.position > 0: # Number of active Long positions
            action = 'SELL' # to offset the long positions
        elif each.position < 0: # Number of active Short positions
            action = 'BUY' # to offset the short positions
        else:
            assert False
        totalQuantity = abs(each.position)
        price = ib.reqMktData(each.contract).bid-0.25
        while math.isnan(price):
            price = ib.reqMktData(each.contract).bid-0.25
            ib.sleep(0.1)
        print(price)
        order = LimitOrder(action, totalQuantity, price) #round(25 * round(/25, 2), 2))
        trade = ib.placeOrder(each.contract, order)
        print(f'Flatten Position: {action} {totalQuantity} {contract.localSymbol}')
        for c in ib.loopUntil(condition=0, timeout=120): # trade.orderStatus.status == "Filled"  or \
            #trade.orderStatus.status == "Cancelled"
            print(trade.orderStatus.status)
            c=len(ib.openOrders())
            print(f'Open orders = {c}')
            if c==0 or trade.orderStatus.status == 'Inactive': 
                print('sell loop finished')
                return
        
    
def option_position():
    stock_owned = np.zeros(2)
    position = ib.positions()
    call_position= None
    put_position = None
    for each in position:
        if each.contract.right == 'C':
            call_position = each.contract
            stock_owned[0] = each.position
        elif each.contract.right == 'P':
            put_position = each.contract
            stock_owned[1] = each.position
    call_position = call_position if call_position != None else res.get_contract('C', 2000)
    put_position = put_position if put_position != None else res.get_contract('P', 2000)
    return stock_owned, call_position, put_position
tickers_signal = "Hold"
buy_index = [] 
sell_index = []
# state, stock_price, cash_in_hand = reset(data, stock_owned, cash_in_hand)
while True:
    
    cash_in_hand = float(ib.accountSummary()[22].value)
    portolio_value = float(ib.accountSummary()[29].value)
    data_raw = res.options(res.options(res.ES(),res.option_history(res.get_contract('C', 2000))),res.option_history(res.get_contract('P', 2000)))
    df = data_raw[['high', 'low', 'volume', 'close', 'RSI', 'ATR', 'roll_max_cp', 'roll_min_cp', 'roll_max_vol','macd', 'macdsignal', 'ES_C_close','ES_P_close']]
    stock_owned, call_contract, put_contract = option_position()
    if tickers_signal == "Hold":
        print('Hold')
        if df["high"].iloc[-1] >= df["roll_max_cp"].iloc[-1] and \
                df["volume"].iloc[-1] > df["roll_max_vol"].iloc[-2] and df['RSI'].iloc[-1] > 30 \
                and df['macd'].iloc[-1] > df['macdsignal'].iloc[-1] :
            buy_index.append(0)
        
        
        
        elif df["low"].iloc[-1] <= df["roll_min_cp"].iloc[-1] and \
                df["volume"].iloc[-1] > df["roll_max_vol"].iloc[-2] and df['RSI'].iloc[-1] < 70 \
                and df['macd'].iloc[-1] < df['macdsignal'].iloc[-1]:
            buy_index.append(1)
        
        
        else:
            buy_index = []
            sell_index = []
    
    elif tickers_signal == "Buy":
        print('BUY SIGNAL')
        if df["close"].iloc[-1] > df["close"].iloc[-2] - (0.75 * df["ATR"].iloc[-2]) and len(ib.positions())!=0:
            sell_index.append(0)
        
        elif df["low"].iloc[-1] <= df["roll_min_cp"].iloc[-1] and \
                df["volume"].iloc[-1] > df["roll_max_vol"].iloc[-2] and df['RSI'].iloc[-1] < 70 \
                and df['macd'].iloc[-1] < df['macdsignal'].iloc[-1] and len(ib.positions())!=0:
            sell_index.append(0)
            buy_index.append(1)
    
    
    elif tickers_signal == "Sell":
        print('SELL SIGNAL')
        if df["close"].iloc[-1] < df["close"].iloc[-2] + (0.75 * df["ATR"].iloc[-2]) and len(ib.positions())!=0:
            sell_index.append(1)
        
        
        elif df["high"].iloc[-1] >= df["roll_max_cp"].iloc[-1] and \
                df["volume"].iloc[-1] > df["roll_max_vol"].iloc[-2] and df['RSI'].iloc[-1] > 30 \
                and df['macd'].iloc[-1] > df['macdsignal'].iloc[-1] and len(ib.positions())!=0:
            sell_index.append(1)
            buy_index.append(0)
            
            
            
    if sell_index:
        for i in sell_index:
            if not stock_owned[i] == 0:
                contract= call_contract if i == 0 else put_contract
                ib.qualifyContracts(contract)
                flatten_position(contract)
            
            cash_in_hand = float(ib.accountSummary()[5].value)
            stock_owned, call_contract, put_contract = option_position()

    if buy_index:
        can_buy = True
        while can_buy:
            
            for i in buy_index:
                contract = call_contract if i == 0 else put_contract
                ib.qualifyContracts(contract)
                stock_price = ib.reqMktData(contract).ask+0.25
                while math.isnan(stock_price):
                    stock_price = ib.reqMktData(contract).ask+0.25
                    ib.sleep(0.1)
                if cash_in_hand > (stock_price * 50 * 2) and cash_in_hand > portolio_value \
                    and ((stock_owned[0] == 0 and i == 0) or (stock_owned[1] == 0 and i == 1)): 
                  quantity = int((cash_in_hand/(stock_price * 50)))
                  
                  order = LimitOrder('BUY', quantity, stock_price) #round(25 * round(stock_price/25, 2), 2))
                  trade = ib.placeOrder(contract, order)
                  no_price_checking = 1
                  for c in ib.loopUntil(condition=0, timeout=120): # trade.orderStatus.status == "Filled"  or \
                      #trade.orderStatus.status == "Cancelled"
                      print(trade.orderStatus.status)
                      print(no_price_checking)
                      no_price_checking+=1
                      c=len(ib.openOrders())
                      print(f'Open orders = {c}')
                      ib.sleep(2)
                      if c==0: break
                  
                  print('out of loop')
                  stock_owned, call_contract, put_contract = option_position()
                  cash_in_hand = float(ib.accountSummary()[5].value)
                  can_buy = False
                else:
                  can_buy = False

    time.sleep(30)