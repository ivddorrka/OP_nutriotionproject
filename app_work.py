# """
# Website v0
# """
# from flask import Flask, redirect, url_for, render_template, request
# from calculator import Calculator
# import random 
# import sys
# from flask_sqlalchemy import SQLAlchemy
# # from menu import Menu 

# sys.setrecursionlimit(10**6)

# # m = Menu(1900, 60, 65, 290, [])
# # m.generate_menu()
# # print(str(m).split('\n\n'))

# # c1 = Calculator(65.5, 167.2, 19, 'F', 1.9)
# # LST = ["menu1", "menu2", "menu3", "menu4", "menu5", "menu6"]

# # def create_index():
# #     first =random.randint(0,100)
# #     second= random.randint(101,200)
# #     third= random.randint(201,300)
# #     summa= sum([13,15, 17])
# #     index = open("templates/base.html").read().format(p3= c1.calories_need(),
# #                                             p5= c1.proteins_need(),
# #                                             p7= c1.fats_need(),
# #                                             p9= c1.carbohydrates_need(),
# #                                             p1= first,
# #                                             p2= second,
# #                                             p10= third,
# #                                             p4= f'All calories: {summa}',
# #                                             p11= 1,
# #                                             p12=2,
# #                                             p13=3,
# #                                             p14=4)

# #     with open('templates/index.html', 'w') as f:
# #         f.write(index) 


# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = '/home/daria/op_project/OP_nutriotionproject/users.db'

# db = SQLAlchemy(app)

# class Menu(db.Model):
#     text = db.Column(db.String(1500))

# m1 = 'apr0'
# m2 = 'owq2'
# m3 = 'pwn3'

# all_m = [m1, m2, m3]

# # for i in range(len(all_m)):
# #     menu = Menu(text=all_m[i], complete=False)
# #     db.session.add(menu)
# #     db.session.commit()



# menu = Menu(text=all_m[0], complete=False)
# db.session.add(menu)
# db.session.commit()

# print(Menu.query.all())
# @app.route("/")
# def home():
#     """
#     Home page
#     """
#     menus = Menu.query.all()
#     return render_template("base.html", menus=menus)

# # @app.route("/next", methods=["POST", "GET"])
# # def next():
# #     menu = Menu(complete=False)
# #     db.session.add()
# #     db.session.commit()

# #     return redirect(url_for('home'))



# # @app.route("/next/check", methods=["POST", "GET"])
# # def next1():
# #     ans = request.form.get("ans")
# #     if ans:
# #         create_index()
# #         next()
# #     return render_template("index.html")



# if __name__ == "__main__":
#     app.run(debug=True)


"""
Website v0
"""
from flask import Flask, session, redirect, url_for, render_template, request
import user_work
import user_db
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
users_db = user_db.UserDB()

@app.route("/")
def home():
    """
    Home page
    """
    username = escape(session['username']) if 'username' in session else False
    users = users_db.users
    return render_template("home.html", title='Home page', username=username, users=users)


@app.route("/", methods=["POST"])
def login():
    """
    This is post request to home page
    """
    try:
        login = request.form['login']
        password = request.form['password']

        if users_db.get(login).password == password:
            session['username'] = request.form['login']
            return redirect(url_for('home', title='Home page', message='Login successful'))
        else:
            return redirect(url_for('home', title='Home page', message='Wrong password'))
    except user_db.UserNotFound:
        return redirect(url_for('home', title='Eror', message='No such user'))


@app.route('/register', methods=['GET'])
def register_page():
    if 'username' not in session:
        return render_template('registration.html')
    else:
        return "Your are already logged in"


@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template("profile.html", title='Profile', username = escape(session['username']), logged_in_status=True)
    return "You are not logged in"


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home', title='Home page', message='Logout successful'))


@app.route('/profile', methods=['POST'])
def profile_update():
    '''
    This route changes user profile
    '''
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    gender = request.form.get("gender")
    act = request.form.get("comp_select")
    # update user info
    return render_template("profile.html")


@app.route("/registration", methods=["POST"])
def infor_user():
    """
    To get data from user
    """
    login = request.form.get("login")
    password = request.form.get("password")
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    gender = request.form.get("gender")
    act = request.form.get("comp_select")
    user = user_work.User(login)
    return user, password, age, height, weight, gender, act


@app.route("/registration/submitted", methods=["POST"])
def file_html():
    """
    To return already submitted page
    """
    info = infor_user()
    password = info[1]
    user = info[0]
    age = info[2]
    height = info[3]
    weight = info[4]
    gender = info[5]
    act = info[6]
    try:
        user.set_characteristics(age, height, weight, gender, act)
        try:
            user.set_password(password)
            users_db.add(user)
            return users_db.__str__()
            return render_template("calc.html")
        except user_work.PasswordTooShortError:
            return render_template("failure.html")
    except ValueError:
        return render_template("failure.html")


if __name__ == "__main__":
    FLASK_DEBUG=1
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
