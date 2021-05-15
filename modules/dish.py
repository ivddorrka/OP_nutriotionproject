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
