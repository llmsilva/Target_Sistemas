#!/usr/bin/env python
# coding: utf-8

# In[1]:


entrada = input('\nDigite a string a ser invertida: ')

l = len(entrada)-1
r = ""

for i in range(l, -1, -1):
    r += entrada[i]

print(f'\nA inversão da string "{entrada}" resulta "{r}".')

