import numpy as np
import matplotlib.pyplot as plt

def nlognfit(x,y):
    """ Ajusta os pares de pontos (xi,yi) a f(x)= a*x*ln(x) + b usando o método
    dos minimos quadrados.
         Entradas:
            x: o vetor contendo as abscissas
            y: o vetor contendo as ordenadas

         Saída: retorna o par de coeficientes em uma lista [a,b]
    """
    z = x * np.log(x)
    coefs = np.polyfit(z,y,1)
    return coefs

def plota_nlogfit(x,y):
    a,b = nlognfit(x,y)
    legenda_ajuste = "${:.3f} x\\ln(x) + {:.3f}$".format(a, b)
    plt.plot(x,y,"o",label="dados")
    plt.plot(x, a * x * np.log(x) + b,"--", label=legenda_ajuste)
    plt.legend(loc='upper left')
    plt.show()

#x = np.array([1.2,  2.8,  4.3,  5.4,   6.8,   7.9])
#y = 4 * x*np.log(x) + 6.45
    
