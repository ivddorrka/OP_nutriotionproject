"""
Module for calculator.
"""


class Calculator:
    """
    Class for calculator.
    """

    def __init__(self, weight: float, height: float, age: int, sex: str, activity: float):
        """
        Initialize a calculator with given characteristics of user.
        Weight is in the kg and height is in the cm.
        """
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
        self.activity = activity

    def calories_need(self) -> float:
        """
        Return the daily amount of calories to this user (in kcal).
        """
        if self.sex == 'M':
            return round((10*self.weight + 6.25*self.height - 5*self.age + 5)*self.activity)
        return round((10*self.weight + 6.25*self.height - 5*self.age - 161)*self.activity)

    def proteins_need(self):
        """
        Return the daily amount of proteins to this user (in grams).
        """
        return round(0.8*self.weight*self.activity)

    def fats_need(self):
        """
        Return the daily amount of calories to this user (in grams).
        """
        return round(0.3*self.calories_need()/9)

    def carbohydrates_need(self):
        """
        Return the daily amount of calories to this user (in grams).
        """
        return round(0.55*self.calories_need()/4)
