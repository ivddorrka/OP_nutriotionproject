"""
Module for implementing menu class.
"""
import csv
import random
from modules.dish import Dish
from modules.product import Product


class Menu:
    """
    Class for menu.
    """

    def __init__(self, calories: float, proteins: float, fats: float, carbohydrates: float, preferences: list):
        """
        Initilaize a menu for user with his/her info about daily intake of nutrients.
        """
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.preferences = preferences
        self.daily_calories = 0
        self.daily_proteins = 0
        self.daily_fats = 0
        self.daily_carbohydrates = 0
        self.menu = []
        self.all_dishes = self.choose_dishes()

    def __str__(self):
        """
        Return info about menu.
        """
        menu = ''
        for dish in self.menu:
            menu += (dish.name + '\n\nProducts: ' + str(dish.products) + '\n\nInsruction: ' +
                     str(dish.instruction) + '\n\nCalories: ' +
                     str(dish.calories) + '\nProteins: ' + str(dish.proteins) +
                     '\nFats: ' + str(dish.fats) +
                     '\nCarbohydrates: ' + str(dish.carbohydrates) + '\n\n' +
                     '-----------------------------------------------------')
        return menu

    def choose_dishes(self):
        """
        Search for the dishes which user will eat. Return list of these dishes.
        """
        possible_dishes = []
        with open("recipes.csv") as recipes_base:
            recipes_csv = csv.reader(recipes_base, delimiter=',')
            for dish in recipes_csv:
                cool_recipe = True
                for bad_food in self.preferences:
                    if bad_food in dish[1]:
                        cool_recipe = False
                        break
                if float(dish[3]) == 0.0 or float(dish[4]) == 0.0 or float(dish[5]) == 0.0 or\
                        float(dish[6]) == 0.0:
                    cool_recipe = False
                if float(dish[3]) > self.calories or float(dish[4]) > self.proteins or float(dish[5]) > self.fats or\
                        float(dish[6]) > self.carbohydrates:
                    cool_recipe = False
                if cool_recipe:
                    possible_dishes.append(Dish(dish[0], dish[2], dish[1], float(dish[3]),
                                                float(dish[4]), float(dish[5]), float(dish[6])))
        return possible_dishes

    def generate_menu(self):
        """
        Generates menu which consists of 3 different dishes to the user.
        """
        calories = 0
        proteins = 0
        fats = 0
        carbohydrates = 0

        # our breakfast's nutrients should be less than 40% of daily intake
        random.shuffle(self.all_dishes)
        for dish in self.all_dishes:
            if (dish.calories <= self.calories * 0.4 and
                dish.proteins <= self.proteins * 0.4 and
                dish.fats <= self.fats * 0.4 and
                    dish.carbohydrates <= self.carbohydrates * 0.4):
                breakfast = dish
                calories += breakfast.calories
                proteins += breakfast.proteins
                fats += breakfast.fats
                carbohydrates += breakfast.carbohydrates
                self.menu.append(breakfast)
                break

        # our lunch's nutrients should be more than 50% of daily intake and less than 90% of daily intake
        for dish in self.all_dishes:
            if (self.calories * 0.5 <= calories + dish.calories <= self.calories * 0.9 and
                    self.proteins * 0.5 <= proteins + dish.proteins <= self.proteins * 0.9 and
                    self.fats * 0.5 <= fats + dish.fats <= self.fats * 0.9 and
                    self.carbohydrates * 0.5 <= carbohydrates + dish.carbohydrates <= self.carbohydrates * 0.9):
                lunch = dish
                calories += lunch.calories
                proteins += lunch.proteins
                fats += lunch.fats
                carbohydrates += lunch.carbohydrates
                self.menu.append(lunch)
                break

        # our dinner's nutrients should be more than 85% of daily intake and less than 115% of daily intake
        for dish in self.all_dishes:
            if (self.calories * 0.85 <= calories + dish.calories <= self.calories * 1.15 and
                    self.proteins * 0.85 <= proteins + dish.proteins <= self.proteins * 1.15 and
                    self.fats * 0.85 <= fats + dish.fats <= self.fats * 1.15 and
                    self.carbohydrates * 0.85 <= carbohydrates + dish.carbohydrates <= self.carbohydrates * 1.15):
                dinner = dish
                calories += dinner.calories
                proteins += dinner.proteins
                fats += dinner.fats
                carbohydrates += dinner.carbohydrates
                self.menu.append(dinner)
                break

        while len(self.menu) != 3:
            self.menu.clear()
            self.generate_menu()

    def generate_dish(self):
        """
        Add new dish to the menu if user wanted to change the current one.
        !Prerequirements: this method generates the third meal, two others stay.
        """
        calories = self.menu[0].calories + self.menu[1].calories
        proteins = self.menu[0].proteins + self.menu[1].proteins
        fats = self.menu[0].fats + self.menu[1].fats
        carbohydrates = self.menu[0].carbohydrates + self.menu[1].carbohydrates

        random.shuffle(self.all_dishes)
        for dish in self.all_dishes:
            if (self.calories * 0.85 <= calories + dish.calories <= self.calories * 1.15 and
                    self.proteins * 0.85 <= proteins + dish.proteins <= self.proteins * 1.15 and
                    self.fats * 0.85 <= fats + dish.fats <= self.fats * 1.15 and
                    self.carbohydrates * 0.85 <= carbohydrates + dish.carbohydrates <= self.carbohydrates * 1.15):
                self.menu.append(dish)

    def delete_dish(self, dish: Dish):
        """
        User refuses to eat this dish, we change it.
        """
        self.menu.remove(dish)
        self.generate_dish()

    def accept_dish(self, dish: Dish):
        """
        User aceepts dish, we substitute his/her daily intake of nutrients by this 
        dish.
        """
        self.daily_calories += dish.calories
        self.daily_proteins += dish.proteins
        self.daily_fats += dish.fats
        self.daily_carbohydrates += dish.carbohydrates

    # user choose product_name and enters the exact_name from list
    def search_product(self, product_name: str) -> list:
        """
        Search for the product in database, return the list of possible products.
        """
        product = Product(product_name)
        possible_list = product.get_products()
        return possible_list

    def choose_product(self, exact_name: str, weight: float):
        """
        Adds info about calories and nutrients
        about product with the given name and weight.
        """
        nutrients = Product('').choose_product(exact_name, weight)
        self.daily_calories += nutrients[0]
        self.daily_proteins += nutrients[1]
        self.daily_fats += nutrients[2]
        self.daily_carbohydrates += nutrients[3]
