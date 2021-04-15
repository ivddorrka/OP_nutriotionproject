'''
Module shows how to work with API we use in our project.
https://www.themealdb.com/api.php
'''
import json
import requests

def get_random_recipe():
    '''
    Get an info about random recipe.
    '''
    return requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()

def get_info_recipe(recipe: dict):
    '''
    Return info about ingridients in recipe.
    '''
    recipe = recipe['meals'][0]
    info = f'{recipe["strMeal"]}\nInstructions: {recipe["strInstructions"]}\n'
    for itr in range(20):
        if recipe[f"strIngredient{itr+1}"]:
            info+=f'{recipe[f"strIngredient{itr+1}"]} - {recipe[f"strMeasure{itr+1}"]}\n'
    return info

if __name__ == '__main__':
    recipe = get_random_recipe()
    print(recipe)
    print(get_info_recipe(recipe))