import json 
import csv
from recipe_analyse import result_ingredients

f = open('recipes/recipes_raw_nosource_ar.json')
data = json.load(f)
random_recipe_id = data
values = list(data.values())

lst_to_csv = [['Title', 'Ingredints', 'Instructions']]
lol = []
# try:
for i in values:
    res = []
    try:
        try:
            try:
                res.append(i['title'])
                res.append(result_ingredients(i['ingredients']))
                res.append(i['instructions'])
            except IndexError:
                continue
        except ValueError:
            continue
    except KeyError:
        continue

    lst_to_csv.append(res)
# except ValueError:
#     lol.append(1)

f = open('recipes3.csv', 'w')

with f:
    writer = csv.writer(f)
    for row in lst_to_csv:
        writer.writerow(row)

f.close()
# print(len(lol))