# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

papeis = ['PG', 'MSFT', 'F', 'GE']
precos = pd.DataFrame()

for p in papeis:
    precos[p] = wb.DataReader(p, data_source='yahoo',
                              start='1995-1-1')['Adj Close']


# %%
precos.info()

# %%
precos.head(10)

# %%
# Normalizar os retornos para ficar mais facil na comparacao
# Todos os papeis vao partir do mesmo ponto (olha a partir dos retornos)
precos.iloc[0]
dados_normlizados = precos/precos.iloc[0] * 100
dados_normlizados.plot(figsize=(12, 6))

# %%
precos.plot(figsize=(12, 6))

# %%
retornos = precos / precos.shift(1)-1

pesos = np.array([0.25, 0.25, 0.25, 0.25])

ponderacao = np.dot(retornos, pesos)

#%%
retorno_anaual = ponderacao.mean() * 250
retorno_carteira = np.dot(retorno_anaual, pesos)
retorno_carteira
