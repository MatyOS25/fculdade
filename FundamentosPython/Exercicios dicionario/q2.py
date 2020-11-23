vetores = []
for i in range (1,6):
    numero = int(input(f"Informe um número inteiro, válido: "))
    while numero <= 0:
        numero = int(input(f"Informe um número inteiro, válido: "))
    vetores.append(numero)
print(vetores)
    