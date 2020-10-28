def elemento_na_lista():
    tupla_exemplo = (1,2,3,4,5,6,7,8)
    elemento = 8
    if elemento in tupla_exemplo:
        return tupla_exemplo.index(elemento)
    else:
        print("Número não se encontra na tupla")
    
print(elemento_na_lista())