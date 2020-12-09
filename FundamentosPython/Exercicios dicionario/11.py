import pandas as pd
import numpy as np

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

dataframe = pd.read_csv(url, sep=',')
frame_genre = dataframe[(dataframe['Genre'] == 'Action') | (dataframe['Genre'] == 'Shooter') | (dataframe['Genre'] == 'Platform')]

print(f"A: {frame_genre.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)}")

global_sales = dataframe.groupby(['Publisher'])['Global_Sales'].sum().sort_values(ascending=False)

print(f"B: {global_sales.head(3)}")

frame_japan_action  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Action')]
d1 = frame_japan_action.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)

print(f"C-1: {d1.head(1)}")

frame_japan_shooter  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Shooter')]
d2 = frame_japan_shooter.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)

print(f"C-2: {d2.head(1)}")

frame_japan_platform  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Platform')]
d3 = frame_japan_platform.groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)

print(f"C-3: {d3.head(1)}")

sales_japan_action  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Action')]
ds1 = sales_japan_action.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

print(f"D-1: {ds1.head(1)}")

sales_japan_shooter  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Shooter')]
ds2 = sales_japan_shooter.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

print(f"D-2: {ds2.head(1)}")

sales_japan_platform  = dataframe[(dataframe['Year_of_Release'] >= 2010) & (dataframe['Genre'] == 'Platform')]
ds3 = sales_japan_platform.groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

print(f"D-3: {ds3.head(1)}")