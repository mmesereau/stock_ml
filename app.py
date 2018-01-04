import pandas as pd
import numpy as np
import plot
import dataframe as dtf
import statistics as st
import writeFiles as wr
import datetime


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
