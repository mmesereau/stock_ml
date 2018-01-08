import pandas as pd
import indicators
import dataframe
import datetime

def inputs(company, begin="2000-01-03", end=datetime.date.today()):
    df = dataframe.get_data([company])
    boll = indicators.bollinger_differential(company)
    rsi = indicators.RSI(company)
    oscillator = indicators.stochastic_oscillator(company)
    input_set = df.join(boll.join(rsi))
    return input_set[20:]


def tomorrow_close (company, begin="2000-01-03", end=datetime.date.today()):
    df = dataframe.get_data([company])
    df.columns = ["Tomorrow's Close"]
    return df.shift(-1)[20:]
