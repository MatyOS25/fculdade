def fatorial_numero_while():
    '''Informa o valor da fatorial de um número positivo (Usando While)'''
    fatorial = int(input("Informe a fatorial: "))
    while fatorial < 0:
        fatorial = int(input("Fatorial Inválida. Digite um valor maior que 0: "))

    valor = fatorial
    decrease = fatorial - 1
    while decrease > 1:
        valor = valor * (decrease)
        decrease -= 1
    
    print(f"O valor da fatorial é: {valor}")

fatorial_numero_while()