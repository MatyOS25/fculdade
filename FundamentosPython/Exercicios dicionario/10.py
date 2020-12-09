import pandas as pd

esportes = ['Skiing', 'Curling', 'Skating', 'Ice Hockey']
paises_escolhidos = ['SWE', 'NOR', 'FIN']
medalhas = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')
medalhas = medalhas\
    .query("NOC in @paises_escolhidos and Sport in @esportes and Year > 2000 and Medal == 'Gold'")\
    .groupby(['NOC'], as_index=False)\
    .count()
    
medalhista = medalhas.sort_values(by=['Medal'], ascending=False).iloc[0]

print(f"O maior medalhista de ouro do século 21 nas modalidades Skiing, Curling, Skating, Ice Hockey foi: {medalhista['NOC']} com {medalhista['Medal']} medalhas")