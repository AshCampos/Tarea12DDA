#Programa que hace una busqueda binaria por medio de particiones
#Se introduce un arreglo de elementos ordenados
#Como salida podemos tener el indice del elemento que se encuentra o un -1 si no está

def busqueda_binaria(A, ele):
    if len(A) == 0:
        return -1

    m = len(A) // 2

    if A[m] == ele:
        return m

    elif A[m] < ele:
        indiceDer = busqueda_binaria(A[m+1:], ele)
        if indiceDer == -1:
            return -1
        else:
            return m + 1 + indiceDer

    else:
        return busqueda_binaria(A[:m], ele)

A = [1, 3, 5, 7, 9, 11, 13, 15, 17]
ele = 15
indice = busqueda_binaria(A, ele)
print(f"El índice del elemento {ele} es: {indice}")
