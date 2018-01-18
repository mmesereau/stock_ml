import pandas as pd
import numpy as np
import datetime
from . import dataframe as dtf
from . import statistics as st
from . import writeFiles as wr
from . import get_companies as gc
from . import constructor
# from . import algorithms
from .algorithms import mlp_regressor as mlp
from .algorithms import update_regressor as update
from .algorithms import use_regressor as use
from .algorithms import get_model_accuracy as accuracy


def get_companies():
    return gc.companies()

def writeFile(name):
    wr.writeFile(name)
    return True

def generate_model(company):
    return mlp.perceptron_regressor(company)

def update_csv(company):
    wr.update_csv(company)
    return True

def clean(company):
    wr.clean(company)
    return True

def update_regressor(company, start="2000-01-03", end=datetime.date.today()):
    data = constructor.inputs(company,start, end).iloc[1:2].as_matrix()
    output = [actual(company)]
    update.update(company, data, output)
    return True

def use_regressor(company, start=datetime.date.today()-datetime.timedelta(1), end=datetime.date.today()):
    data = constructor.inputs(company, start, end).iloc[0:1].as_matrix()
    output = use.use(company, data)
    prevClose = prevDay(company, datetime.date.today())
    return [output[0], prevClose]

def actual(company):
    full = dtf.get_data([company])
    return full[company][0]


def prevDay(company, date):
    full = dtf.get_data([company])
    return full[company].as_matrix()[0]

def get_model_accuracy(company):
    return accuracy.get_accuracy(company)

# MSFT_data = dtf.get_data(["MSFT"], "2017-01-01")
# rolling_MSFT_mean = st.rolling_mean("MSFT", 20, "2017-01-01")
# rolling_MSFT_std = st.rolling_standard_deviation("MSFT", 20, "2017-01-01")
# MSFT_lower_band = st.bollinger_lower(rolling_MSFT_mean, rolling_MSFT_std)
# MSFT_upper_band = st.bollinger_upper(rolling_MSFT_mean, rolling_MSFT_std)
# MSFT_daily_return = st.daily_return("MSFT", "2017-01-01")
# # plot.graph([MSFT_daily_return])
# begin = "2017-01-01"
# end = datetime.date.today()
# print(st.sharpe_ratio("MSFT", begin, end))
# # print(dtf.get_data(["MSFT"]))
# # print("MSFT has gained " + str(st.cumulative_return("MSFT", begin)) + " percent since " + begin)
# # plot.graph([MSFT_data, rolling_MSFT_mean, MSFT_lower_band, MSFT_upper_band])
