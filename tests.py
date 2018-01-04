import constants
import dataframe
import indicators
import plot
import statistics
import writeFiles
import pandas as pd

company = "MSFT"
df = dataframe.get_data([company])
boll = indicators.bollinger_differential(company)
rsi = indicators.RSI(company)
oscillator = indicators.stochastic_oscillator(company)

# data = pd.concat([df, boll.to_frame()])
data = df.join(boll.join(rsi))
print(data[400:])

plot.graph([df[40:], boll[40:], rsi[40:], oscillator[40:]])
