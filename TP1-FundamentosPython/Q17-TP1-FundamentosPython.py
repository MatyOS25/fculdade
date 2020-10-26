def mover_esquerda_string():
    valor = int(input("Valor numérico: "))
    palavra = input("Uma string/palavra: ")

    tras = palavra[:valor]
    frente = palavra[valor:]
    completo = frente + tras
    print(completo)

mover_esquerda_string()