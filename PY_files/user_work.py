"""User class example"""

class User:
    """To get info from user"""
    def __init__(self, age, height, weight, gender, activity):
        """Init function"""
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity = activity

    def set_characteristics(self):
        """To set all characteristics"""
        self.get_age()
        self.get_height()
        self.get_weight()

    def get_age(self):
        """To get age"""
        self.age = int(self.age)
        
    def get_height(self):
        """To get height"""
        self.height = int(self.height)


    def get_weight(self):
        """To get weight"""
        self.height = int(self.height)
    
    def get_activ(self):
        """To get a number of activity"""
        self.activity = float(self.activity.split()[0])
        
            
if __name__=="__main__":
    us = User()
    us.set_characteristics()