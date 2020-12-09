valor_max = int(input("Informe o valor máximo: "))
valor_soma = 0
for n in range(1, valor_max + 1):
    if n % 2 == 0:
        valor_soma += n
print(f"Soma dos números entre 1 e {valor_max} é de: {valor_soma}")