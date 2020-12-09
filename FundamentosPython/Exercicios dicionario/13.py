import requests, re
from collections import Counter
from bs4 import BeautifulSoup

request = requests.get('http://brasil.pyladies.com/about')
request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text,"lxml")

num_ladies = 0
total_words = 0
words = []

for elemento in bs.html.body.article.find_all('div'):
    num_ladies += elemento.text.lower().count('ladies')
    for word in elemento.text.split():
        word = re.sub('\W+', '', word)
        words.append(word.lower())

total_words = len(words)
words_dict = dict(Counter(words))

print('Total de words no corpo da página:', total_words)

for word, counter in words_dict.items():
    if(counter == 1):
        print(f"A palavra '{word}' apareceu somente uma vez na página")

print("\n", 'Total de vezes "ladies" na página:', num_ladies)