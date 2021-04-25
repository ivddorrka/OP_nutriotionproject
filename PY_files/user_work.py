"""User class example"""

class User:
    def __init__(self):
        self.age = None
        self.height = None
        self.weight = None
        self.sex = None
        self.activity = None
    def set_characteristics(self):
        self.get_age()
        self.get_height()
        self.get_weight()
        self.get_sex()
        self.get_activity()
    def get_age(self):
        age = input("Enter your age here: ")
        try:
            self.age = int(age)
        except ValueError:
            print("Invalid age!")
            return self.get_age()
    def get_height(self):
        height = input("Enter your height here: ")
        try:
            self.height = int(height)
        except ValueError:
            print("Invalid height!")
            return self.get_height()
    def get_weight(self):
        weight = input("Enter your weight here: ")
        try:
            self.weight = int(weight)
        except ValueError:
            print("Invalid weight!")
            return self.get_weight()
    def get_sex(self):
        sex_choice = "F\nM"
        print(sex_choice)
        sex = input("Choose your sex here: ")

        if sex in sex_choice.split('\n'):
            self.sex = sex
        else:
            print("Invalid choise!")
            return self.get_sex()
    def get_activity(self):
        var = ["1.2 - Sedentary: Little or no physical activity.\n",
            "1.3 - Lightly Active: Light exercise or activity 1-3 days per week.",
            "1.5 - Moderately Active: Moderate exercise or activity 3-5 days per week.",
            "1.7 - Very Active: Hard exercise or activity 6-7 days per week.",
            "1.9 - Extremely Active: Hard daily exercise or activity and physical work\n"]
        print("Choose your activities level")
        lst = [1.2, 1.3, 1.5, 1.7, 1.9]
        print('\n'.join(var))
        answer = input("Enter it's number: ")
        # print(var)
        try:
            self.activity = float(answer)
            if self.activity not in lst:
                print("Doesn't exist!\nTry again!")
                return self.get_activity()
        except ValueError:
            print("Wrong variant, try again")
            return self.get_activity()

us = User()
us.set_characteristics()
print(us.age)
print(us.height)
print(us.weight)
print(us.sex)
print(us.activity)