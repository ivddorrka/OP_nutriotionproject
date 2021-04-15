'''
Module shows how to work with API we use in our project.
https://fdc.nal.usda.gov/
'''
import requests
import json

def get_info(product: str):
    '''
    Return an info in .json format about given product.
    '''
    params = {'api_key': '9OdUhuqegMl7QDYKpzz9qBzqThdwgYMAlkjrogFM', #insert your API here
    'query': product,
    'dataType': 'Survey (FNDDS)'}
    response = requests.get(
        f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={params["api_key"]}\
&query={params["query"]}&dataType={params["dataType"]}') 
    return response.json()

def get_nutrients(product: str):
    '''
    Return the nutrients info of the first type of product in .json file.
    '''
    response = get_info(product)
    food = response["foods"][0]
    info = f'Name: {food["lowercaseDescription"]}\n'
    for nutrient in food["foodNutrients"]:
        if 1000 < nutrient["nutrientId"] < 1010:
            info+= f'{nutrient["nutrientName"]}: {nutrient["value"]} {nutrient["unitName"]}\n'
    info += 'Portion: 100 G'
    return info

if __name__ == '__main__':
    product = input('Enter the product: ')
    # print(get_info(product))
    print(get_nutrients(product))