import re
frases = []
ativo = True
x = 0
while ativo:
    frase = input(f"Informe uma frase: ")
    if frase == 'sair' :
        ativo = False
    else : 
        frases.append(frase)
for i in frases:
    if bool(re.search(r'\beu\b', frase.lower())):
        print(f"A frase \"{frase}\" possui \"eu\"")
