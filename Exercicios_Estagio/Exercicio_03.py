#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_json('dados.json')

df1 = df[df["valor"] != 0]

minimo = df1["valor"].min()
maximo = df1["valor"].max()
media = df1["valor"].mean()
dias = df1[df1["valor"] > media].value_counts().sum()


print(f'\nO menor valor de faturamento diário foi R$ {minimo:.2f}.')
print(f'\nO maior valor de faturamento diário foi R$ {maximo:.2f}.')
print(f'\nEm {dias} dias do mês o faturamento foi maior que a média mensal (que foi igual a R$ {media:.2f}).')

