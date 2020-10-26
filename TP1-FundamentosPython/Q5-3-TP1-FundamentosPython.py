def remover_iten_tupla():
    tupla_exemplo = (1,2,3,4,5,6,7,8)
    print(tupla_exemplo)
    tupla_exemplo = list(tupla_exemplo)
    tupla_exemplo.remove(2)
    tupla_exemplo = tuple(tupla_exemplo)
    print(tupla_exemplo)

remover_iten_tupla()
