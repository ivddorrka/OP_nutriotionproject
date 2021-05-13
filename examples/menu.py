"""
Module for implementing menu class.
"""
import csv
import random
from dish import Dish
from product import Product


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
        self.menu = []

    def __str__(self):
        """
        Return info about menu.
        """
        menu = ''
        for dish in self.menu:
            menu += (dish.name + '\ncalories = ' +
                     str(dish.calories) + '\nproteins = ' + str(dish.proteins) +
                     '\nfats = ' + str(dish.fats) +
                     '\ncarbohydrates = ' + str(dish.carbohydrates) + '\n\n')
        return menu

    def choose_dishes(self):
        """
        Search for the dishes which user will eat. Return list of these dishes.
        """
        possible_dishes = []
        with open("recipes2_new.csv") as recipes_base:
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

        all_dishes = self.choose_dishes()

        # сніданок рандомно обираємо але так, щоб калораж був у межах
        # 20-37.5% від денної норми калорій.
        random.shuffle(all_dishes)
        for dish in all_dishes:
            if (dish.calories <= self.calories * 0.4 and
                dish.proteins <= self.proteins * 0.4 and
                dish.fats <= self.fats * 0.4 and
                    dish.carbohydrates <= self.carbohydrates * 0.4):
                breakfast = dish
                del all_dishes[all_dishes.index(breakfast)]
                calories += breakfast.calories
                proteins += breakfast.proteins
                fats += breakfast.fats
                carbohydrates += breakfast.carbohydrates
                self.menu.append(breakfast)
                break

        # обід зі сніданком має займати 60-80% калорій, білків, жирів та вуглеводів.
        for dish in all_dishes:
            if (self.calories * 0.5 <= calories + dish.calories <= self.calories * 0.9 and
                    self.proteins * 0.5 <= proteins + dish.proteins <= self.proteins * 0.9 and
                    self.fats * 0.5 <= fats + dish.fats <= self.fats * 0.9 and
                    self.carbohydrates * 0.5 <= carbohydrates + dish.carbohydrates <= self.carbohydrates * 0.9):
                lunch = dish
                del all_dishes[all_dishes.index(lunch)]
                calories += lunch.calories
                proteins += lunch.proteins
                fats += lunch.fats
                carbohydrates += lunch.carbohydrates
                self.menu.append(lunch)
                break

        # вечерю обираємо так, щоб калорії були в межах 95-105% від денної норми,
        # білки та вуглеводи - 90-110%, а жири - 90-105%.
        for dish in all_dishes:
            if (self.calories * 0.85 <= calories + dish.calories <= self.calories * 1.15 and
                    self.proteins * 0.85 <= proteins + dish.proteins <= self.proteins * 1.15 and
                    self.fats * 0.85 <= fats + dish.fats <= self.fats * 1.15 and
                    self.carbohydrates * 0.85 <= carbohydrates + dish.carbohydrates <= self.carbohydrates * 1.15):
                dinner = dish
                del all_dishes[all_dishes.index(dinner)]
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
        all_dishes = self.choose_dishes()
        calories = self.menu[0].calories + self.menu[1].calories
        proteins = self.menu[0].proteins + self.menu[1].proteins
        fats = self.menu[0].fats + self.menu[1].fats
        carbohydrates = self.menu[0].carbohydrates + self.menu[1].carbohydrates

        for dish in random.shuffle(all_dishes):
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
        self.calories -= dish.calories
        self.proteins -= dish.proteins
        self.fats -= dish.fats
        self.carbohydrates -= self.carbohydrates

    # user choose product_name and enters the exact_name from list, сайт
    def search_product(self, product_name: str):
        """
        Search for the product in database.
        """
        product = Product(product_name)
        possible_list = product.get_products()
        print(possible_list)  # сайт
        exact_name = input()  # сайт
        nutrients = product.choose_product(exact_name)
        self.calories -= nutrients[0]
        self.proteins -= nutrients[1]
        self.fats -= nutrients[2]
        self.carbohydrates -= nutrients[3]
