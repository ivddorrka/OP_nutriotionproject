"""
Module for adding info about nutrients in each recipe.
"""
import csv
from fuzzywuzzy import fuzz


def product_info(product: str):
    """
    Return the tuple of info about product in comfotable way.
    >>> product_info('black pepper : 1 num')
    ('pepper', '1', 'num')
    >>> product_info('garlic powder : 17.07 g')
    ('powder', '17.07', 'g')
    >>> product_info(': 17.07 g')

    """
    info = product.strip().split(':')
    if len(info) != 2:
        return None
    info[0] = info[0][:-1]
    info[1] = info[1][1:]
    info[1] = info[1].split(' ')
    info[0] = info[0].split(' ')
    return [info[0], info[1][0], info[1][1]]


def search_id(product: str):
    """
    Return the id of product from food.csv table.
    >>> search_id('mango')
    ['1102633', '1102670', '1102671', '1102672', '1102772', '1102870']
    >>> search_id('garlic powder')
    []
    """
    with open("food.csv") as food_base:
        food_base_csv = csv.reader(food_base, delimiter=',')
        list_of_foods = []
        for row in food_base_csv:
            if fuzz.token_set_ratio(row[2], product) > 80:
                list_of_foods.append(row[0])
        return list_of_foods


def nums_to_grams(product_ids: list, num_product: str):
    """
    Return the quantity of product in grams (translates nums in grams).
    """
    with open("food_portion.csv") as food_portion:
        food_portion_csv = csv.reader(food_portion, delimiter=',')
        for row in food_portion_csv:
            for product_id in product_ids:
                if product_id in row[0]:
                    return (float(num_product)*float(row[2]), product_id)
    return (None, None)


def nutrients_gram(product_id: str, amount: str):
    """
    Return info about nutrients in given amount of grams of this product
    (calories, fibers, lipids, carbohydrates).
    """
    nutrient_info = [0, 0, 0, 0]
    with open("food_nutrient.csv") as food_nutrients:
        food_nutrients_csv = csv.reader(food_nutrients, delimiter=',')
        for row in food_nutrients_csv:
            if product_id == row[0]:
                if row[1] == '1008':
                    nutrient_info[0] = (float(row[2])*float(amount)/100.0)
                if row[1] == '1003':
                    nutrient_info[1] = (float(row[2])*float(amount)/100.0)
                if row[1] == '1004':
                    nutrient_info[2] = (float(row[2])*float(amount)/100.0)
                if row[1] == '1005':
                    nutrient_info[3] = (float(row[2])*float(amount)/100.0)
    return nutrient_info


def main(path: str, write_file: str):
    '''
    Adding info to the file.
    '''
    with open(path) as our_file, open(write_file, 'w') as write_file:
        csv_reader = csv.reader(our_file)
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            cool_recipe = True
            calories = 0
            proteins = 0
            lipids = 0
            carbohydrates = 0
            products = row[1].split('\n')
            for product in products:
                info = product_info(product)
                if not info:
                    cool_recipe = False
                else:
                    product_ids = search_id(info[0])
                    if product_ids:
                        if info[2] == 'num':
                            info[1] = nums_to_grams(product_ids, info[1])[0]
                            correct_id = nums_to_grams(product_ids, info[1])[1]
                        else:
                            correct_id = product_ids[0]
                        if not info[1]:
                            cool_recipe = False
                        else:
                            if nutrients_gram(correct_id, info[1]) == [0, 0, 0, 0]:
                                cool_recipe = False
                            else:
                                calories += nutrients_gram(correct_id,
                                                           info[1])[0]
                                proteins += nutrients_gram(correct_id,
                                                           info[1])[1]
                                lipids += nutrients_gram(correct_id,
                                                         info[1])[2]
                                carbohydrates += nutrients_gram(
                                    correct_id, info[1])[3]
            if cool_recipe:
                csv_writer.writerow(
                    [row[0], row[1], row[2], calories, proteins, lipids, carbohydrates])


if __name__ == '__main__':
    main('recipes3.csv', 'recipes2_new.csv')
