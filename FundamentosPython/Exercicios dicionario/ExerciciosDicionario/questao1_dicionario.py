def lista_sem_duplicadas(lista):
    lista_nova = []
    teste = 0
    for item in lista:
        if item in lista_nova:
            teste = 1
        else: 
            lista_nova.append(item)
    print(lista_nova)
lista = [1,1,2,2,3,4,2,5,6]
lista_sem_duplicadas(lista)