def lista_sem_duplicadas(lista):
    lista = sorted(set(lista))
    print(lista)
lista = [1,1,2,2,3,4,2,5,6]
lista_sem_duplicadas(lista)