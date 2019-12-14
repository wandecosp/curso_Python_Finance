# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

# %%
PG.head()

PG["retorno"] = (PG["Adj Close"]/PG["Adj Close"].shift(1))-1

# %%
PG["retorno"].plot(figsize=(10, 5))


# %%
# Calculo dos Retornos Simples
media_retornos = PG["retorno"].mean()
print(media_retornos)
media_retornos *= 250
print(str(round(media_retornos * 100, 2)) + '%')


# %%
# Calculo do log retorno - serie temporal quandos e avalia um unico ativo
log_retorno = np.log(PG["Adj Close"]/PG["Adj Close"].shift(1))
log_retorno2 = np.log(PG["retorno"] + 1)
PG["log_retorno"] = np.log(PG["retorno"] + 1)

# %%
log_retorno.head()

# %%
log_retorno2.head()

# %%
#comparo os retornos simples com os log retornos
retornos = pd.DataFrame(PG, columns=['retorno', 'log_retorno'])
retornos.head()
retornos.plot(figsize=(10, 5))
# %%