#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
porcentagem = []
total = sum(faturamento)

for i in range(len(estados)):
    porcentagem.append(f'{round(faturamento[i]*100/total,2)} %')

dic = {"Estado": estados, "Faturamento (R$)": faturamento, "Participação": porcentagem}
dados = pd.DataFrame(data=dic)

display(dados)

