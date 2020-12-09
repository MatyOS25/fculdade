numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,30,27,23,45,28)
def par_impar(numeros):
    pares = []
    impares = []
    for index, n in enumerate(numeros):
        if index % 2 == 0:
            pares.append(n)
        if n % 2 != 0:
            impares.append(n)
    pares = tuple(pares)
    print(impares, pares)
par_impar(numeros)