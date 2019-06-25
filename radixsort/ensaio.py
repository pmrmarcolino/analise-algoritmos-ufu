import numpy as np
import argparse

from radixsort import *

parser = argparse.ArgumentParser()
parser.add_argument("arq_vetor",
                    help="nome do arquivo contendo o vetor de teste")
args = parser.parse_args()

# Lê o arquivo contendo o vetor e passado na linha de comando como um
# vetor do Numpy.

vet = np.loadtxt(args.arq_vetor)
radixsort(vet)
