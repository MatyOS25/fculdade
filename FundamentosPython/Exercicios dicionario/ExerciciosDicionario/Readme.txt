Computa¸c˜ao I - Python
Laborat´orio 10
1. Escreva uma fun¸c˜ao que recebe uma lista e retorna uma nova lista sem elementos duplicados. Lembre
que os elementos duplicados n˜ao precisam aparecer em posi¸c˜oes consecutivas. Dica: use um dicion´ario.
2. Escreva uma fun¸c˜ao que converte n´umeros inteiros entre 1 e 999 para algarismos romanos. N˜ao converta
o n´umero para uma string, e use um la¸co while. Use os trˆes dicion´arios abaixo:
• UNIDADES = { 0: ”, 1: ’I’, 2: ’II’, 3: ’III’, 4: ’IV’, 5: ’V’, 6: ’VI’, 7: ’VII’, 8: ’VIII’, 9: ’IX’ }
• DEZENAS = { 0: ”, 1: ’X’, 2: ’XX’, 3: ’XXX’, 4: ’XL’, 5: ’L’, 6: ’LX’, 7: ’LXX’, 8: ’LXXX’, 9:
’XC’ }
• CENTENAS = { 0: ”, 2: ’C’, 2: ’CC’, 3: ’CCC’, 4: ’CD’, 5: ’D’, 6: ’DC’, 7: ’DCC’, 8:’DCCC’,
9:’CM’ }
3. Construa uma fun¸c˜ao que receba uma string e retorne um dicion´ario onde cada palavra dessa string seja
uma chave e tenha como valor o n´umero de vezes que a palavra aparece. Por exemplo:
freq palavras(“dinheiro ´e dinheiro e vice versa”)
retorna o dicion´ario:
{ “dinheiro”:2, “´e”: 1 ,“e”: 1, “vice”: 1, “versa”:1}
4. Sabe-se que uma mol´ecula de RNA mensageiro ´e utilizada como base para sintetizar prote´ınas, no
processo denominado de tradu¸c˜ao. Cada trinca de bases de RNA mensageiro est´a relacionado com um
amino´acido. Combinando v´arios amino´acidos, temos uma prote´ına. Com base na tabela (simplificada)
de trincas de RNA abaixo, crie uma fun¸c˜ao que receba uma string representando uma mol´ecula de RNA
mensageiro v´alida, segundo essa tabela, e retorne a cadeia de amino´acidos que representam a prote´ına
correspondente:
Trinca de RNA Nome do Amino´acido
UUU Phe
CUU Leu
UUA Leu
AAG Lisina
UCU Ser
UAU Tyr
CAA Gln
Exemplo: traducao rnaM(“UUUUUAUCU”) retorna “Phe-Leu-Ser”
1
Computa¸c˜ao I - Python Laborat´orio 10
5. Escreva uma fun¸c˜ao que recebe uma lista de compras e um dicion´ario contendo o pre¸co de cada produto
dispon´ıvel em uma determinada loja, e retorna o valor total dos itens da lista que estejam dispon´ıveis
nesta loja. Por exemplo, para os dados:
lista_de_compras = ’biscoito’, ’chocolate’, ’farinha’
supermercado = {
’amaciante’:4.99,
’arroz’:10.90,
’biscoito’:1.69,
’cafe’:6.98,
’chocolate’:3.79,
’farinha’:2.99
}
O valor retornado pela fun¸c˜ao ser´a 8.47.
6. Afinidades entre pessoas podem ser descritas atrav´es de dicion´arios, por exemplo se tivermos:
• Leo gosta de Sofia,
• Marcos gosta de Andrea,
• Sofia gosta de Leo,
• Alex gosta de Andrea, e
• Andrea gosta de Marcos
Podemos representar estas rela¸c˜oes atrav´es do dicion´ario:
afinidades = {
’Leo’: ’Sofia’,
’Marcos’: ’Andrea’,
’Sofia’: ’Leo’,
’Alex’: ’Andrea’,
’Andrea’: ’Marcos’
}
Escreva uma fun¸c˜ao que recebe um dicion´ario de afinidades e retorna uma lista de pares com afinidade
m´utua, ou seja, onde um gosta do outro. Por exemplo, para o dicion´ario acima, a fun¸c˜ao deve retornar:
[(’Marcos’, ’Andrea’), (’Sofia’, ’Leo’)]