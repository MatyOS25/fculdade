def fatorial_numero():
    '''Informa o valor da fatorial de um número positivo'''
    fatorial = int(input("Informe a fatorial: "))
    while fatorial < 0:
        fatorial = int(input("Fatorial Inválida. Digite um valor maior que 0: "))

    valor = fatorial
    for atual in range(fatorial, 1, -1):
        valor = valor * (atual-1)
    
    print(f"O valor da fatorial é: {valor}")

fatorial_numero()

        
