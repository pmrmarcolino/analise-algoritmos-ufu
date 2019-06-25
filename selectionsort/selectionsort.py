import numpy as np

@profile
def selectionsort( lista ):
    for i in range( len( lista ) ):
        least = i
        for k in range( i + 1 , len( lista ) ):
            if lista[k] < lista[least]:
                least = k
        troca( lista, least, i )

def troca( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
