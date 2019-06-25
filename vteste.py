
from math import *
import random
import numpy as np

def embaralha(m,v,n):
    """Embaralha m elementos centrais do vetor v de tamanho n."""
    m = ceil(m)
    if m > 0 and m <= n:
       mi = (n-m) // 2
       mf = (n+m) // 2
       for num in range(mi,mf):
           i = np.random.randint(mi,mf)
           j = np.random.randint(mi,mf)
           t = v[i]
           v[i] = v[j]
           v[j] = t
    return v


def cria(n, percentual=0, tipo='int', inf=-1000, sup=1000):
    """Cria um vetor com tamanho n contendo números inteiros (default)
       ou em ponto flutuante, entre inf e sup.
       Entradas:
       n - tamanho do vetor a ser criado;
       percentual - determina como o vetor criado estará ordenado:
         -1: vetor em ordem decrescente
          1: vetor em ordem crescente
          0: vetor aleatório
          0 < percentual < 1.0: vetor parcialmente ordenado em ordem
              crescente com o percentual dos elementos em torno do 
              centro ordenados aleatoriamente.
         -1 < percentual < 0 vetor parcialmente ordenado em ordem
              decrescente, com o percentual dos elementos em torno do 
              centro ordenados aleatoriamente.
       tipo - 'int' para inteiro ou 'float' para ponto flutuante;
       inf - menor valor para um elemento do vetor
       sup - maior valor para um elemento do vetor
    """ 

    if percentual < 0.0:
        v = np.linspace(sup, inf, num=n)
        if tipo == 'int':
           v = np.trunc(v)

        if percentual <= -1.0:
            return v
        else:
            return embaralha(-percentual*n, v, n)
    elif percentual > 0.0:
        v = np.linspace(inf, sup, num=n)
        if tipo == 'int':
           v = np.trunc(v)

        if percentual >= 1.0:
            return v
        else:
            return embaralha(percentual*n, v, n)
    else:
        return np.random.randint(inf, sup, size=n)



