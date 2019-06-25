import os
import shutil

# Arquivo de configuração do ensaio
from config import controle

dir_modelo = './modeloRelatorio'

def cria_modelo():
    if not os.path.isdir(dir_modelo):
        os.makedirs(dir_modelo)
    arqmodelo = dir_modelo + '/modelo.tex'
    shutil.copyfile('./cabecalho.tex',arqmodelo)

    ftex = open(arqmodelo, mode='a', encoding='utf-8')

    for ensaio in controle:
        num_figuras = 0
        diretorio = ensaio['diretorio']
        arqensaio = '/'.join(['..', diretorio, 'ensaio.py'])
        arqmetodo = '/'.join(['..', diretorio, diretorio + '.py'])
        num_graficos = len(ensaio['graficos']['eixos'])

        # Escreve as tabelas e os gráficos
        dir_tabelas =  '/'.join(['.', diretorio, 'tabelas'])
        dir_graficos = '/'.join(['.', diretorio, 'imagens'])

        if not os.path.isdir(dir_tabelas):
           print("O diretório 'tabelas' de " + diretorio +
                  ' não foi encontrado')
           raise

        if not os.path.isdir(dir_graficos):
           print("O diretório 'imagens' de " + diretorio +
                  ' não foi encontrado')
           raise
        tabelas = [ fn for fn in next(os.walk(dir_tabelas))[2]]
        arqs_tabs = [ os.path.join(dir_tabelas, fn) for fn in tabelas]

        arqs_tabs.sort()
        for atab in arqs_tabs:
            ftex.write('\\input{.'+ atab + '}\n\n')
            grafico = atab.split('/')[-1].split('.')[0]
            for i in range(num_graficos):
                num_figuras += 1
                arq_grafico = dir_graficos + '/' + grafico + str(i) + '.png'
                ftex.write('\\begin{figure}[ht]\n')
                ftex.write('\\centering \\includegraphics[scale=0.8]{.' +
                           arq_grafico + '}\n')
                ftex.write('\caption{Explique o gráfico: ' + grafico + str(i) +
                           '.png}\n')
                ftex.write('\\label{fig:' + grafico + str(i) + '}\n')
                ftex.write('\\end{figure}\n\n')
            if num_figuras % 10 == 0:
                ftex.write('\\clearpage\n')
            else:
                ftex.write('\n')
        ftex.write('\\clearpage\n')

    escreve_cab_apendice = True
    for ensaio in controle:
        num_figuras = 0
        diretorio = ensaio['diretorio']
        arqensaio = '/'.join(['..', diretorio, 'ensaio.py'])
        arqmetodo = '/'.join(['..', diretorio, diretorio + '.py'])

        # Escreve nos apêndices os códigos usados
        if escreve_cab_apendice:
            ftex.write('\\clearpage\n')
            ftex.write('\\addcontentsline{toc}{part}{Apêndice}\n')
            ftex.write('\\appendix\n\n')
            escreve_cab_apendice = False

        capitulo = ''.join(['\chapter{Arquivo ', arqmetodo, ' \label{ap:',
                            diretorio, '}}\n'])
        listing = ''.join(['\lstinputlisting[caption={', arqmetodo,
                           ' \label{arq:', diretorio, '}}]{', arqmetodo,
                           '}\n\n'])
        ftex.write(capitulo)
        ftex.write(listing)

        capensaio = ''.join(['\chapter{Arquivo ', arqensaio, ' \label{ap:',
                             diretorio, 'ensaio}}\n'])
        listensaio = ''.join(['\lstinputlisting[caption={', arqensaio,
                              ' \label{arq:', diretorio, 'ensaio}}]{',
                              arqensaio, '}\n\n'])
        ftex.write(capensaio)
        ftex.write(listensaio)
    ftex.write('\\end{document}')
    ftex.close()


cria_modelo()
