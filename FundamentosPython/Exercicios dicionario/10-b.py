import pandas as pd

data_frame = pd.read_csv(
    'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv', sep=',')


medalha_maior = data_frame[(data_frame['NOC'] == 'SWE') | (
    data_frame['NOC'] == 'DEN') | (data_frame['NOC'] == 'NOR')]


ano_filtro = medalha_maior[(medalha_maior['Year'] >= 2001)]

sports_filter = ano_filtro[(ano_filtro['Sport'] == 'Curling') | (ano_filtro['Sport'] == 'Skating') | (
    ano_filtro['Sport'] == 'Skiing') | (ano_filtro['Sport'] == 'Ice Hockey')]

filter_medals_of_gold = sports_filter[sports_filter['Medal'] == 'Gold']

maior_medalhista_ouro_filtro = filter_medals_of_gold.groupby(
    ['NOC'])['Medal'].count().sort_values()
print(maior_medalhista_ouro_filtro)