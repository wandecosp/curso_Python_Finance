#%%
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

# %%
PG.head()

