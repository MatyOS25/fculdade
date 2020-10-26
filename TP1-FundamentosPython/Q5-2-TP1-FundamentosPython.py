def elemento_na_tupla():
    tupla = (1,2,3,4,5,6)

    half = len(tupla)//2

    another_half = len(tupla) - half

    tupla1 = tupla[:half]
    tupla2 = tupla[another_half:]

    print('tupla1: ', tupla1)
    print('tupla2: ', tupla2)

elemento_na_tupla()
