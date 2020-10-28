def traducao(busca):
    trinca = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr', 'CAA': 'Gln'}
    resultado = []
    for index in range(0, len(busca) // 3):
        valor = busca[index*3:(index*3)+3]
        resultado.append(trinca[valor]) 
    print('-'.join(resultado))
traducao(input("Digite a trinca para busca, 9caract: "))
