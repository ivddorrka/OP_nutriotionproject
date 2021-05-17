"""
Module for implementing class dish.
"""
from dataclasses import dataclass


@dataclass
class Dish:
    """
    Class for dishes.
    """
    name: str
    instruction: str
    products: str
    calories: float
    proteins: float
    fats: float
    carbohydrates: float

    def __str__(self):
        """
        Representation of dish.
        """
        return f"""{self.name}\n
Products: {self.products} \n
Instruction: {self.instruction}\n
Calories: {round(self.calories, 2)}\n
Proteins: {round(self.proteins, 2)}\n
Fats: {round(self.fats, 2)}\n
Carbohydrates: {round(self.carbohydrates, 2)}\n
        """

