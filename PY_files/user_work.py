"""User class example"""

class User:
    """To get info from user"""
    def __init__(self, login, password):
        """Init function"""
        self.age = None
        self.height = None
        self.weight = None
        self.gender = None
        self.activity = None
        self.login = login
        self.password = password

    def set_characteristics(self, age, height, weight, gender, act):
        """To set all characteristics"""
        self.get_age(age)
        self.get_height(height)
        self.get_weight(weight)
        self.get_activ(act)


    def get_age(self, age):
        """To get age"""
        self.age = int(age)
        
    def get_height(self, height):
        """To get height"""
        self.height = int(height)


    def get_weight(self, weight):
        """To get weight"""
        self.weight = int(weight)
    
    def get_activ(self, act):
        """To get a number of activity"""
        self.activity = float(act.split()[0])
        
            
# if __name__=="__main__":
#     us = User()
#     us.set_characteristics()