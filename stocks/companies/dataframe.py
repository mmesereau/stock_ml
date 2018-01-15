import pandas as pd
import matplotlib.pyplot as plt
import datetime


def get_data(symbols, start_date="2000-01-03", end_date=datetime.date.today(), column="adjusted_close"):
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    for item in symbols:
        df_temp = pd.read_csv("companies/companies/" + item + ".csv", index_col="timestamp",
                                parse_dates=True, usecols=["timestamp", column],
                                na_values=['nan']).rename(columns={"adjusted_close": item})
        if len(symbols) > 1:
            df1 = df1.join(df_temp, how="inner")
        else:
            df1 = df_temp
    return df1

def slicing_data(dataframe, start, end, companies):
    return dataframe.ix[start:end, companies]

def normalize_data(dataframe):
    return dataframe / dataframe.ix[0, :]

def plot_data(df, title):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Relative Price")
    plt.show()
