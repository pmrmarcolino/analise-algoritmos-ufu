import os
import numpy as np

# Arquivo de configuração do ensaio
from config import controle

# Ajuste de curvas usando o método dos mínimos quadrados
from ajuste import ajuste
from plotagem import plota

for ensaio in controle:
    diretorio = ensaio['diretorio']
    dir_resultado =  '/'.join(['.', diretorio, 'resultados'])
    if not os.path.isdir(dir_resultado):
        print('Diretorio de dados {}, nao encontrado.'.format(dir_resultado))
        raise

    dir_grafico =  '/'.join(['.', diretorio, 'imagens'])
    if not os.path.isdir(dir_grafico):
        os.makedirs(dir_grafico)

    complexidade_pior_caso   = ensaio['complexidade']['pior']
    complexidade_melhor_caso = ensaio['complexidade']['melhor']
    complexidade_caso_medio  = ensaio['complexidade']['medio']

    legenda_experimento = ensaio['graficos']['legenda_experimento']
    eixos = ensaio['graficos']['eixos']

    def gera_grafico(caso):
        for instancia in ensaio['instancias'][caso]:
            arqdados = "/".join([dir_resultado, diretorio + instancia + '.dat'])
            print('Plotando os gráficos para ' + arqdados)
            dados = np.loadtxt(arqdados, unpack=True)
            for g,i in zip(eixos,range(len(eixos))):
                xcol = g['abscissa']['col']
                ycol = g['ordenada']['col']
                xs = dados[xcol]
                ys = dados[ycol]
                fn_ajustada, legenda_fn = ajuste(complexidade_pior_caso, xs, ys)
                arqgrafico = "/".join([dir_grafico,
                                       diretorio + instancia + str(i) + '.png'])

                rotulo_eixo_x = g['abscissa']['rotulo']
                rotulo_eixo_y = g['ordenada']['rotulo']
                plota(arqgrafico, xs, ys,
                      rotulo_eixo_x, rotulo_eixo_y,
                      legenda_experimento,
                      legenda_fn,
                      fn_ajustada)

    gera_grafico('pior')
    gera_grafico('medio')
    gera_grafico('melhor')
