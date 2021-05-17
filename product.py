"""
Module for implementing product class.
"""
import requests


class Product:
    """
    Class for product.
    """

    def __init__(self, name: str):
        """
        Initialize a product with its name.
        """
        self.name = name

    def get_products(self):
        """
        Return the list of the names of the products which API found by users ask.
        """
        list_of_products = []
        params = {'api_key': '9OdUhuqegMl7QDYKpzz9qBzqThdwgYMAlkjrogFM',
                  'query': self.name,
                  'dataType': 'Survey (FNDDS)'}
        response = requests.get(
            f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={params["api_key"]}\
&query={params["query"]}&dataType={params["dataType"]}')
        response = response.json()
        for food in response["foods"]:
            list_of_products.append(food["lowercaseDescription"])
        return list_of_products

    def choose_product(self, exact_name: str, weight: float):
        """
        Return the info about nutrients (as a tuple in order calories-lipids-fats
        -carbohydrates) in this exact product.
        Weight should be in grams!
        """
        nutrients = [0, 0, 0, 0]
        params = {'api_key': '9OdUhuqegMl7QDYKpzz9qBzqThdwgYMAlkjrogFM',
                  'query': exact_name,
                  'dataType': 'Survey (FNDDS)'}
        response = requests.get(
            f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={params["api_key"]}\
&query={params["query"]}&dataType={params["dataType"]}')
        response = response.json()
        food = response["foods"][0]
        for nutrient in food["foodNutrients"]:
            if nutrient["nutrientId"] == 1008:
                nutrients[0] = weight*float(nutrient["value"])/100
            if nutrient["nutrientId"] == 1003:
                nutrients[1] = weight*float(nutrient["value"])/100
            if nutrient["nutrientId"] == 1004:
                nutrients[2] = weight*float(nutrient["value"])/100
            if nutrient["nutrientId"] == 1005:
                nutrients[3] = weight*float(nutrient["value"])/100
        return tuple(nutrients)


if __name__ == "__main__":
    pr = Product('ham')
    last = pr.get_products()
    # print(pr.choose_product(last, 25.6))
    print(last)