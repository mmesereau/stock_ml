import pandas as pd
import numpy as np
import dataframe as dfr
import datetime
import statistics

def bollinger_differential(company, window=20, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    mean = pd.rolling_mean(df[company], window=window)
    stdev = pd.rolling_std(df[company], window=window)
    boll = ((mean - df[company]) / stdev).to_frame()
    boll.columns = ["Bollinger Differential"]
    return boll

def RSI(company, window=14, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    change = df[1:] - df[:-1].values
    rsi = df
    for item in range(len(df[company])):
        gains = 0
        losses = 0
        for index in change[company][item - window:item]:
            if index > 0:
                gains += item
            elif index < 0:
                losses += item
        if losses == 0:
            rsi[company][item] = None
        else:
            rsi[company][item] = 100 - (100 / (1 + (gains / losses)))
    rsi.columns = ["RSI"]
    return rsi

def stochastic_oscillator(company, window=14, begin="2000-01-03", end=datetime.date.today()):
    closes = dfr.get_data([company], begin, end)
    lows = dfr.get_data([company], begin, end, "low")
    highs = dfr.get_data([company], begin, end, "high")
    oscillators = closes
    for index in range(len(closes[company])):
        high = closes[company][index]
        low = closes[company][index]
        for item in lows["low"][(index - window):index]:
            if item < low:
                low = item
        for item in highs["high"][(index - window):index]:
            if item > high:
                high = item
        total = 100 * (closes[company][index] - low) / (high - low)
        
        if index > window:
            oscillators[company][index] = total
        else:
            oscillators[company][index] = None
    oscillators.columns = ["Stochastic Oscillator"]
    return oscillators
