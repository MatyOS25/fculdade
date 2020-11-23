vetores = []
tamanho_vetor = int(input(f"Numero de vezes para executar: "))
while tamanho_vetor <= 0 :
    tamanho_vetor = int(input(f"Numero de vezes para executar: "))
for n in range(0,tamanho_vetor):
    numero = int(input(f"Informe um número inteiro ({n+1} de {tamanho_vetor}): "))
    while numero <= 0:
        numero = int(input(f"Informe um número inteiro ({n+1} de {tamanho_vetor}): "))
    vetores.append(numero)
print(f"Existem {vetores.count(0)} zeros na lista.")