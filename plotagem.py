import numpy as np
import matplotlib.pyplot as plt

# Arquivo de configuração do ensaio
from config import controle


def plota(arqgraf, x, y, rotx, roty, legenda_exp, legenda_f, f):
    # Plota a curva experimental
    plt.plot(x, y, 'ro', label=legenda_exp)

    # Plota a curva teórica
    xs = np.linspace(x[0],x[-1]+20,num=32)
    plt.plot(xs, f(xs), label=legenda_f)

    # Posiciona a legenda
    plt.legend(loc='upper left')

    # Rotula os eixos
    plt.xlabel(rotx)
    plt.ylabel(roty)
    plt.savefig(arqgraf)
    plt.close()
