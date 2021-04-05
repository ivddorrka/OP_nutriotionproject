"""
This is what we need from *.json recipes files
"""
import json 
import random 

f = open('recipes_raw_nosource_ar.json')
data = json.load(f)
random_recipe_id = random.choice(list(data))
info = data[random_recipe_id]
print(info['title']) #title of a meal
print('\n')
print(info['instructions']) # instructions how to cook
print('\n')
print('\n'.join(info['ingredients'])) # to get ingredients for this meal
f.close()