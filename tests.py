import constants
import dataframe
import indicators
import plot
import statistics
import writeFiles
import pandas as pd
import constructor
from algorithms import network, mlp_regressor
import numpy as np


def nantest(company):
    data = constructor.inputs(company)

    for index in range(data.shape[0]):
        for column in range(data.shape[1]):
            if np.isnan(data.iloc[index][column]) or not np.isfinite(data.iloc[index][column]):
                print(type(data.iloc[index][column]), index, column, data.iloc[index][column])


# company = "MSFT"
# df = dataframe.get_data([company])
# boll = indicators.bollinger_differential(company)
# rsi = indicators.RSI(company)
# oscillator = indicators.stochastic_oscillator(company)
#
# # data = pd.concat([df, boll.to_frame()])
# data = df.join(boll.join(rsi))
# print(data[400:])
#
# plot.graph([df[40:], boll[40:], rsi[40:], oscillator[40:]])

mlp_regressor.perceptron_regressor("BABA")
