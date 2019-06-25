def trocaElementos(A,x,y):
    aux = A[y]
    A[y] = A[x]
    A[x] = aux

def maxHeapify(A,n,i):
    esquerda = 2*i + 1
    direita = 2*i +2 

    if esquerda < n and A[esquerda] > A[i]:
        maior = esquerda
    else:
        maior = i
    if direita < n and A[direita] > A[maior]:
        maior = direita
    if maior!=i:
        trocaElementos(A,i,maior)
        maxHeapify(A,n,maior)

def constroiMaxHeap(A,n):
    for i in range(n // 2, -1, -1):
        maxHeapify(A,n,i)


@profile
def heapsort(A):
    n = len(A)
    constroiMaxHeap(A,n)
    m = n
    for i in range((n-1), 0, -1):
        trocaElementos(A,0,i)
        m = m - 1
        maxHeapify(A,m,0)
