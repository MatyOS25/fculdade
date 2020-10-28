def numeros_romanos(valor):
    unidades = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX' }
    dezenas = { 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC' }
    centenas = { 0: '', 2: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8:'DCCC', 9:'CM' }
    valor_cent = valor // 100
    valor_dez = (valor - valor_cent*100) // 10
    valor_uni = valor - (valor_cent*100) - (valor_dez*10)
    print(f"{centenas[valor_cent]}{dezenas[valor_dez]}{unidades[valor_uni]}")


numeros_romanos(int(input("Insira de 1 até 999: ")))