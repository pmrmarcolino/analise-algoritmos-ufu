import math

def intercala(A,p,q,r):
	B = [0] *len(A)
	for i in range(p,(q+1)):
		B[i] = A[i]
	for j in range(q+1,(r+1)):
		B[r+q+1-j] = A[j]
	i = p
	j = r
	for k in range (p,(r+1)):
		if(B[i] <= B[j]):
			A[k] = B[i]
			i = i+1
		else:
			A[k] = B[j]
			j = j-1
def merge(A):
	mergesort(A,0,len(A)-1)

@profile
def mergesort(A,esquerda,direita):
	if(esquerda<direita):
		meio = math.floor((esquerda+direita)/2)
		mergesort(A,esquerda,meio)
		mergesort(A,meio+1,direita)
		intercala(A,esquerda,meio,direita)
