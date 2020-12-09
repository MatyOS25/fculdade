import requests
from bs4 import BeautifulSoup

request = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')

request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text,"lxml")

tabela = bs.html.body.find('div', {'class': 'tabela'})

print(tabela.text)