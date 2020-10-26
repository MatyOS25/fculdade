def inverter_tupla():
    tupla_exemplo = (1,2,3,4,5,6,7,8,9)
    print(tupla_exemplo)
    tupla_exemplo = list(tupla_exemplo)
    tupla_exemplo = tupla_exemplo[::-1]
    tupla_exemplo = tuple(tupla_exemplo)
    print(tupla_exemplo)

inverter_tupla()