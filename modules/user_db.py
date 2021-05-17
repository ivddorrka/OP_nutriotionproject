'''
UserDB class
'''
from user_work import User

class UserNotFound(Exception):
    '''
    Raises when trying to access user which is not in UserDB
    '''
    def __init__(self, usr_login):
        super().__init__(f'\'{usr_login}\' is not found in database')
        self.usr_login = usr_login

class UserAlreadyExists(Exception):
    '''
    Raises when trying to add existing user or user with the same login
    '''
    def __init__(self, usr_login):
        super().__init__(f'\'{usr_login}\' is already in database')
        self.usr_login = usr_login


class UserDB:
    '''
    User DataBase class
    '''
    def __init__(self):
        self.users = []


    def get(self, usr_login:str) -> User:
        '''
        Returns User object for usr_login if user with usr_login is in UserDB.
        Otherwise raises UserNotFound exception
        '''
        for user in self.users:
            if user.login == usr_login:
                return user

        raise UserNotFound(usr_login)


    def add(self, user:User):
        '''
        Adds a User to database

        If user with the same login is already in UserDB, UserAlreadyExists exceptoin will be raised
        '''
        if user in self.users:
            raise UserAlreadyExists(user.login)
        self.users.append(user)

    def pop(self, usr_login):
        '''
        Removes a user from database.
        usr_login - user login as str OR object of type User

        If usr_login is represented as object of type User, usr.login will be extracted and
        used to find and delete the user from self.users

        In case user with user_id is not found, UserNotFound exception will be raised
        '''
        login = usr_login.login if isinstance(usr_login, User) else usr_login
        for user in self.users:
            if user.login == login:
                self.users.remove(user)
                return user

        raise UserNotFound(usr_login)

    def clear(self):
        '''
        Removes all users from database
        '''
        self.users.clear()

    def __str__(self):
        return f'UserDB({", ".join([user.login for user in self.users])})'

