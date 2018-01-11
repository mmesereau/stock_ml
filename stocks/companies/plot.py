import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graph(data):
    for item in data:
        item.plot()
    plt.show()
