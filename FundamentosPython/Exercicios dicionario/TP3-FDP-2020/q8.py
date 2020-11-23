import random

trocas = 100
resultados = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}
for n in range(0, trocas):
    resultado = random.randint(1, 6)

    resultados[f"{resultado}"] += 1

for lado in resultados:
    print(f"O número {lado} teve {resultados[lado]} ocorrência{'s' if resultados[lado] > 1 else ''}.")
