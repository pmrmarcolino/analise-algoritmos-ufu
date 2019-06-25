# Lê os vetores usados no teste;
# Para cada vetor:
# - executa o teste como um subprocesso com duração máxima de 5 minutos;
# - processa a saída do teste e escreve o resultado para um arquivo apropriado;

import subprocess
import os
import numpy as np
import re
from datetime import datetime
from math import floor
from functools import reduce

# Arquivo de configuração do ensaio
from config import controle

# Lista com os nomes de todos os diretórios que contenham um programa a ser
# ensaiado. Cada diretório deve conter, além do programa propriamente dito, um
# outro arquivo de nome 'ensaio.py' contendo as instruções sobre o ensaio a ser
# realizado.

dir_vetores = "./vetores" # diretório contendo os arquivos com vetores de teste

if not os.path.isdir(dir_vetores):
    print("O diretório 'vetores' não foi encontrado!")
    raise

def sub_dirs(d):
  sds = [ sd for sd in next(os.walk(os.path.join(dir_vetores,d)))[1] ]
  if sds == []:
     return [os.path.join(dir_vetores,d)]
  else:
     return [os.path.join(dir_vetores,d,sd) for sd in sds]

# Lê o nome de todos os subdiretórios presentes no diretório 'vetores'
diretorios_vet = [ d for d in next(os.walk(dir_vetores))[1]]
diretorios_vet = [ d for sd in map(sub_dirs, diretorios_vet) for d in sd]
diretorios_vet.sort()

dic_dirvets = {}
for d in diretorios_vet:
    # Lê o nome de todos os arquivos no diretório 'vetores/dir', cada um
    # contendo um vetor de teste.
    vet_arqs = [ os.path.join(d, fn)
                 for fn in next(os.walk(d))[2]]
    vet_arqs.sort()

    regex = r".+_(\d+)\.dat"
    tamanhos = 2 ** np.array([ int(re.search(regex,vet).group(1))
                               for vet in  vet_arqs])
    dic_dirvets[d] = list(zip(vet_arqs, tamanhos))


def executa():
    """ Executa uma sequência de testes para cada diretório e para cada vetor.
         linha: número da linha no arquivo gerado pelo line_profiler contendo
                os dados de interesse. Por exemplo, para o BubbleSort, na linha
               15, coluna 'Hits', está o número total de comparações realizadas.
        num_ensaios: número de vezes que cada ensaio será repetido.
    """
    for ensaio in controle:
        diretorio = ensaio['diretorio']
        # verifica se no diretório existe um arquivo de nome 'ensaio.py'
        arqensaio = '/'.join(['.', diretorio, 'ensaio.py'])
        print('\n')
        print('===============================================================')
        print('Ensaiando com o arquivo {}'.format(arqensaio))
        print('===============================================================')

        if not os.path.isfile(arqensaio):
            print("No subdiretório {} não foi encontrado o arquivo "
                  "'ensaio.py'".format(diretorio))
            raise

        dir_resultados =  '/'.join(['.', diretorio, 'resultados'])
        if not os.path.isdir(dir_resultados):
           os.makedirs(dir_resultados)


        dir_tabelas =  '/'.join(['.', diretorio, 'tabelas'])
        if not os.path.isdir(dir_tabelas):
           os.makedirs(dir_tabelas)
        else:
            # remove todas as tabelas antigas
            for f in os.listdir(dir_tabelas):
                os.remove('/'.join([dir_tabelas,f]))


        for subdir in dic_dirvets.keys():
            ds = subdir.split('/')
            if len(ds) < 4:
                prefixo = ds[2]
            else:
                prefixo = ds[2] + ds[3]

            arqdados = "/".join([dir_resultados, diretorio+prefixo+".dat"])
            f = open(arqdados, mode='w', encoding='utf-8')

            arqtabela = "/".join([dir_tabelas, diretorio+prefixo+".tex"])
            ftab = open(arqtabela, mode='w', encoding='utf-8')

            print("\nEscrevendo os resultados para '{}'".format(arqdados))
            rotulos = ensaio['rotulos']

            str_rot = reduce(lambda a, b: a + ' ' + b,
                                     [' {r['+ str(i) +']:>13}'
                                      for i in range(len(rotulos))], '')
            str_contr = '#{:>7} ' + str_rot + ' {t:>20}\n'
            caption = str_contr.format('n',r=rotulos, t='tempo(s)')
            f.write(caption)

            # Cabeçalho da tabela em Latex
            ftab.write('\\begin{table}[ht]\n')
            ftab.write('\\centering\n')
            alinhamento = ''.join(['r' for i in range(len(rotulos) + 2)])
            ftab.write('\\begin{tabular}{' + alinhamento + '} \\toprule\n')
            str_rot = reduce(lambda a, b: a + ' & ' + b,
                                     [' {r['+ str(i) +']:>13}'
                                      for i in range(len(rotulos))], '')
            str_contr = '{:>9}' + str_rot + ' & {t:>14} \\\\ \\midrule\n'
            caption = str_contr.format('n',r=rotulos, t='tempo(s)')
            ftab.write(caption)


            linhas_de_interesse = ensaio['linhas_de_interesse']
            num_ensaios = ensaio['num_de_ensaios']
            print('subdir {}'.format(subdir))

            for arq,tam in  dic_dirvets[subdir]:
                # Monta a linha de comando para o line_profiler usando o arquivo
                # de ensaio e o nome do vetor de teste.
                print('arquivo: {} tam:{}'.format(arq,tam))
                cmd = ' '.join(["kernprof -l -v", arqensaio, arq])

                print("Executando {} com o vetor em '{}'".format(diretorio,arq))
                # Tempo máximo de execução do programa para este vetor: cinco
                # minutos
                tempo_max = 5 * 60  # em segundos

                tempo_total = []
                for vezes in range(num_ensaios):
                    try:
                        saida_texto = subprocess.check_output(cmd,
                                                              shell=True,
                                                              universal_newlines=True,
                                                              stderr=subprocess.STDOUT,
                                                              timeout=tempo_max)
                    except subprocess.TimeoutExpired:
                        print("O vetor em '{}' consumiu muito tempo".format(arq))
                        medicoes = [float("inf")] * len(linhas_de_interesse)
                        tempo_total = [float("inf")] * num_ensaios
                        break
                    except subprocess.CalledProcessError:
                        f.close()
                        print("Erro ao ensair {} com o vetor em '{}', verifique seu "
                                 "arquivo 'ensaio.py'".format(diretorio,arq))
                        raise
                    else:
                        linhas = saida_texto.split('\n')
                        unidade_tempo = float(linhas[1].split()[2])
                        tempo_total.append( float(linhas[3].split()[2]))
                        ls_inter = [linhas[nlinha-1].split()
                                    for nlinha in linhas_de_interesse]
                        medicoes = [int(li[1]) for li in ls_inter]

                tempo_total.sort()     # ordena para pegar a mediana

                str_med = reduce(lambda a, b: a + ' ' + b,
                                     [' {m['+ str(i) +']:>13}'
                                      for i in range(len(medicoes))], '')
                str_contr = '{n:>8} ' + str_med + ' {t: >#13.6f}'
                str_res = str_contr.format(n=tam, m=medicoes,
                                           t=tempo_total[floor(num_ensaios/2)])
                print(str_res)
                f.write(str_res + '\n')
                f.flush()

                # Escreve uma linha tabela Latex
                str_med = reduce(lambda a, b: a + ' & ' + b,
                                     [' {m['+ str(i) +']:>13}'
                                      for i in range(len(medicoes))], '')
                str_contr = '{n:>8} ' + str_med + ' & {t: >#13.6f}'
                str_res = str_contr.format(n=tam, m=medicoes,
                                           t=tempo_total[floor(num_ensaios/2)])
                ftab.write(str_res + ' \\\\\n')
                ftab.flush()
            f.close()

            # Fechamento da tabela do Latex
            ftab.write('\\bottomrule\\addlinespace\n')
            ftab.write('\\end{tabular}\n')
            texto = diretorio+prefixo
            ftab.write('\\caption{' + 'Explique essa tabela: '+ texto + '}\n')
            ftab.write('\\label{tab:' + texto + '}\n')
            ftab.write('\\end{table}\n')
            ftab.close()
            try: os.remove('./ensaio.py.lprof')
            except FileNotFoundError: pass

def temporiza():
    agora = datetime.now()
    print("\nEnsaio iniciado em {}/{}/{} às {} h {} min {} s".format(
        agora.day, agora.month, agora.year,
        agora.hour, agora.minute, agora.second))

    executa()

    depois = datetime.now()
    print("\nEnsaio terminado em {}/{}/{} às {} h {} min {} s".format(
        depois.day, depois.month, depois.year,
        depois.hour, depois.minute, depois.second))

    duracao = depois - agora
    horas, resto = divmod(duracao.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    print("Duracao total: {} h {} min {} s".format(horas, minutos, segundos))


# Chamada
temporiza()
