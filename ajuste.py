import numpy as np

from expfit import expfit
from logfit import logfit
from nlognfit import nlognfit


def legenda_poli(coefs):
    rot = 'T(n) = '
    termos = [ ('{:.4g}'.format(c), i)
               for c,i in zip(coefs,reversed(range(len(coefs))))
               if not np.isclose(c, 0.0)]
    inicio = True
    for c,i in termos:
        if inicio:
            if i == 0:
                rot += c
            elif i == 1:
                rot += c + 'n'
            else:
                rot += c + 'n^{' +  str(i) + '}'
            inicio = False
        else:
            if i == 0:
                rot += ' + ' + c
            elif i == 1:
                rot += ' + ' + c + 'n'
            else:
                rot += ' + ' + c + 'n^{' +  str(i) + '}'
    return rot

def legenda_nln(a,b):
    rot = 'T(n) = '
    if not np.isclose(a, 0.0):
        rot += str(a) + 'n\\ln(n)'
        if not np.isclose(b, 0.0):
            rot += ' + ' + str(b)
    else:
        rot += str(b)
    return rot

def legenda_ln(a,b):
    rot = 'T(n) = '
    if not np.isclose(a, 0.0):
        rot += str(a) + '\\ln(n)'
        if not np.isclose(b, 0.0):
            rot += ' + ' + str(b)
    else:
        rot += str(b)
    return rot

def legenda_en(a,b):
    rot = 'T(n) = '
    if not np.isclose(a, 0.0):
        if not np.isclose(b, 0.0):
            rot += str(a) + 'e^{' + str(b) + 'n}'
        else:
            rot += str(a)
    else:
        rot += '0.0'
    return rot


def ajuste(fn, x, y):
    """ Calcula os coeficientes de um ajuste usando o método dos mínimos
         quadrados.
         Entradas:
            fn: uma string indicando a forma da função a ser ajustada.
            x: o vetor contendo as abscissas.
            y: o vetor contendo as ordenadas.
         Saída:  a função ajustada e uma legenda para ela. A legenda poderá ser
                 usada em um gráfico do matplotlib.
    """

    if fn == 'n':
        # Ajusta os coeficientes de um polinômio de grau 1
        coefs = np.polyfit(x, y, 1)
        f = np.poly1d(coefs)
        legenda = legenda_poli(coefs)
    elif fn == 'n^2':
        # Ajusta os coeficientes de um polinômio de grau 2
        coefs = np.polyfit(x, y, 2)
        f = np.poly1d(coefs)
        legenda = legenda_poli(coefs)
    elif fn == 'nln(n)':
        # Ajusta os coeficientes a e b da função  f(n)= a*n*ln(n) + b
        coefs = nlognfit(x, y)
        a,b = coefs
        f = lambda n: a * n * np.log(n) + b
        legenda = legenda_nln(a,b)
    elif fn == 'ln(n)':
        # Ajusta os coeficientes a e b da função  f(n)= a*ln(n) + b
        coefs = logfit(x, y)
        a,b = coefs
        f = lambda n: a * np.log(n) + b
        legenda = legenda_ln(a,b)
    elif fn == 'e(n)':
        # Ajusta os coeficientes a e b da função  f(n)= ae^(bx)
        coefs = expfit(x, y)
        a,b = coefs
        f = lambda n: a * np.exp(b*n)
        legenda = legenda_en(a,b)
    else:
        print("A função 'ajuste' nao esta preparada para ajustar " + fn)
        raise
    return (f, '$' + legenda + '$')
