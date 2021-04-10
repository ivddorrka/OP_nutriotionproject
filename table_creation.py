import json 
import pandas as pd
import csv

f = open('small_recipe.json')
data = json.load(f)
random_recipe_id = data
values = list(data.values())

lst_to_csv = [['Title', 'Ingredints', 'Instructions']]

for i in values:
    res = []
    res.append(i['title'])
    res.append(i['ingredients'])
    res.append(i['instructions'])
    lst_to_csv.append(res)

f = open('recipes.csv', 'w')

with f:
    writer = csv.writer(f)
    for row in lst_to_csv:
        writer.writerow(row)
