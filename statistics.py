import pandas as pd
import numpy as np
import dataframe as dfr
import datetime



def rolling_mean(company, window=20, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    return pd.rolling_mean(df[company], window=window)

def rolling_standard_deviation(company, window=20, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    return pd.rolling_std(df[company], window=window)

def bollinger_lower(rm, rstd):
    return rm - rstd * 2

def bollinger_upper(rm, rstd):
    return rm + rstd * 2

def daily_return(company, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    return (df[1:] / df[:-1].values) - 1

def cumulative_return(company, begin="2000-01-03", end=datetime.date.today()):
    df = dfr.get_data([company], begin, end)
    return ((df[company][-1] / df[company][0]) - 1) * 100

def mean_daily_return(company, begin="2000-01-03", end=datetime.date.today()):
    values = daily_return(company, begin, end)
    return np.mean(values)

def std_daily_return(company, begin="2000-01-03", end=datetime.date.today()):
    values = daily_return(company, begin, end)
    return np.std(values)

def sharpe_ratio(company, begin="2000-01-03", end=datetime.date.today(), window=252):
    return int(window) ** (0.5) * mean_daily_return(company, begin, end) / std_daily_return(company, begin, end)
