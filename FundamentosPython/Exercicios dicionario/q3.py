words = []
for i in range(1,11):
    palavra = input(f"Informe uma palavra: ")
    words.append(palavra)
for word in words:
    print(word[::-1])