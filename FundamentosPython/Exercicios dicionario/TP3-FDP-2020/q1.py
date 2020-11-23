lista = []
x = 1
for y in range(5):
  lista.append(x)
  x += 1
print(lista)
if 3 in lista:
  lista.remove(3)
elif 6 in lista:
  lista.remove(6)
else:
  x = 1
print(lista)
print(len(lista))
lista[3] = 6
print(lista)