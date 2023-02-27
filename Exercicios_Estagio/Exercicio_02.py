#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fib(n):
    seq = [0, 1]
    i = 2
    x = 0
    while x < n + 1:
        seq.append(seq[i - 1] + seq[i - 2])
        x = seq[i]
        i += 1
    seq.pop()
    return seq


n = int(input('Número a ser pesquisado: '))

if n in fib(n):
    print(f'\nO número {n} PERTENCE à sequência de Fibonacci.')
else:
    print(f'\nO número {n} NÃO PERTENCE à sequência de Fibonacci.')

print(f'\nObs.: sequência de Fibonacci até o número dado:\n\n{fib(n)}')

