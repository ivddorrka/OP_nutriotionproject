"""User class 1""" 


class PasswordTooShortError(Exception):
    """To raise when password's too short"""
    pass

class User:
    """To get info from user"""
    def __init__(self, login):
        """Init function"""
        self.age = None
        self.height = None
        self.weight = None
        self.gender = None
        self.activity = None
        self.login = login
        self.password = None
        self.current_menu = None

    def set_characteristics(self, age, height, weight, gender, act):
        """To set all characteristics"""
        try:
            self.get_age(age)
            self.get_height(height)
            self.get_weight(weight)
            self.get_activ(act)
            self.set_gender(gender)
            return True
        except ValueError:
            return False
    
    def set_password(self, password):
        if len(password) < 8:
            raise PasswordTooShortError("Password is too short")
        else:
            self.password = password

    def get_age(self, age):
        """To get age"""
        self.age = int(age)
        
    def get_height(self, height):
        """To get height"""
        self.height = float(height)


    def get_weight(self, weight):
        """To get weight"""
        self.weight = float(weight)
    
    def get_activ(self, act):
        """To get a number of activity"""
        self.activity = float(act.split()[0])

    def set_gender(self, gender):
        """To set a choosen gender"""
        self.gender = gender
        
    def set_current_menu(self, menu):
        self.current_menu = menu

