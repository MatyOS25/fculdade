import requests
from bs4 import BeautifulSoup

estados_centro_oeste = ['df', 'mt', 'go', 'ms']

def mostra_informacao_estado(uf):
    if not uf:
        return

    request = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
    # a linha abaixo é para resolver o problema de encoding
    request.encoding = request.apparent_encoding
    bs = BeautifulSoup(request.text,"lxml")

    linhas = bs.html.body.article.find_all('div', {'class': 'linha'})

    for linha in linhas:
        sigla_estado = linha.find_all('div', {'class': 'celula'})[0].text
        if sigla_estado.lower() == uf.lower():
            print(linha.text)
            return

    print('O estado informado não faz parte do Centro Oeste.')

while True:
    data = input(f"Informe a sigla de um estado do Centro Oeste: ")

    if data and data.lower() in estados_centro_oeste:
        mostra_informacao_estado(data)
        break
    else:
        print('O estado informado não faz parte do Centro Oeste.')