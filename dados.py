import os
import numpy as np

from vteste import cria

def gera_vetores_de_teste(k, k0=5, tipo='int'):
    """ Cria vetores de testes com tamanhos n= 2^k0, 2^(k0+1), ..., 2^k.
        k0: expoente inicial;
        k:  expoente final;
        tipo - o tipo dos elementos do vetor:
               'int' para inteiro
               'float' para ponto flutuante
    """

    # Verifica se existe um diretório com nome 'vetores'.
    # Se não existir, um novo será criado.
    nomedir = "./vetores"
    if not os.path.isdir(nomedir) :
        os.makedirs(nomedir)

    if tipo == 'int':
        formato = '%d'
    else:
        formato = '%f'

    def cria_e_salva_vetor(tam, prefixo, expoente, perc=0):
          if prefixo == 'Crescente':
              percentual = 1
              prefixo2 = prefixo
          elif prefixo == 'Decrescente':
              percentual = -1
              prefixo2 = prefixo
          elif prefixo == 'Aleatorio':
              percentual = 0
              prefixo2 = prefixo
          elif prefixo == 'QuaseCresc':
              percentual = perc  / 100.0
              prefixo2 = "/".join([prefixo, str(perc)])
          elif prefixo == 'QuaseDecresc':
              percentual =  - perc  / 100.0
              prefixo2 = "/".join([prefixo, str(perc)])
          else:
              print("O prefixo {} nao foi reconhecido\n".format(prefixo))
              raise

          vet = cria(tam, percentual, tipo)

          diretorio_vet = os.path.join(nomedir, prefixo2)
          if not os.path.isdir(diretorio_vet):
              os.makedirs(diretorio_vet)

          expoente = '{0:02d}'.format(expoente)
          if perc == 0:
              nomearq = "".join(["v", prefixo,  "_", expoente, ".dat"])
          else:
              nomearq = "".join(["v", prefixo, str(perc), "_", expoente, ".dat"])

          caminho = os.path.join(diretorio_vet, nomearq)
          np.savetxt(caminho, vet, fmt=formato)

    for j in range(k0,k+1):
        tam = 2 ** j
        # vetor em ordem crescente
        cria_e_salva_vetor(tam, 'Crescente',  j)

        # vetor em ordem decrescente
        cria_e_salva_vetor(tam, 'Decrescente',  j)

        # vetor aleatório
        cria_e_salva_vetor(tam, 'Aleatorio',  j)

        # vetor quase ordenado em ordem crescente com 10% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseCresc',  j, 10)

        # vetor quase ordenado em ordem crescente com 20% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseCresc',  j, 20)

        # vetor quase ordenado em ordem crescente com 30% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseCresc',  j, 30)

        # vetor quase ordenado em ordem crescente com 40% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseCresc',  j, 40)

        # vetor quase ordenado em ordem crescente com 50% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseCresc',  j, 50)

        # vetor quase ordenado em ordem decrescente com 10% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseDecresc',  j, 10)

        # vetor quase ordenado em ordem decrescente com 20% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseDecresc',  j, 20)

        # vetor quase ordenado em ordem decrescente com 30% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseDecresc',  j, 30)

        # vetor quase ordenado em ordem decrescente com 40% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseDecresc',  j, 40)

        # vetor quase ordenado em ordem decrescente com 50% de elementos
        # centrais fora do lugar
        cria_e_salva_vetor(tam, 'QuaseDecresc',  j, 50)

# Chamada
gera_vetores_de_teste(13, 5, 'int')
#gera_vetores_de_teste(7, 5, 'int')
