def potencia():
    base = int(input("Qual o valor da base? "))
    while base < 0 :
        base = int(input("Valor inválido, qual o valor da base(maior que zero)? "))
    expoente = int(input("Qual o valor do expoente? "))
    while expoente < 0 :
        expoente = int(input("valor inválido, qual o valor do expoente(maior que zero)? "))
    resultado = base
    for n in range(1, expoente):
        resultado *= base
    if expoente == 0 :
        print(f"{base} elevado na {expoente} dá: 1")
    else: 
        print(f"{base} elevado na {expoente} dá: {resultado}")

potencia() 