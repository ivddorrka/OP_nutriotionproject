"""
Website v0
"""
from flask import Flask, session, redirect, url_for, render_template, request
import user_work
import user_db
from markupsafe import escape
from calculator import Calculator
from product import Product
from menu import Menu

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def backup_user(login, password, height, weight, age, gender, activity, current_menu):
    with open('users.csv', 'a') as f_users:
        f_users.write(
            ','.join([login, password, height, weight, age, gender, activity, 'Nan']))
        f_users.write('\n')


def get_backuped_users():
    with open('users.csv', 'r') as f_users:
        for line in f_users:
            if line.strip():
                attribs = line.split(',')
                user = user_work.User(attribs[0])

                user.set_password(attribs[1])
                user.set_characteristics(
                    attribs[4], attribs[2], attribs[3], attribs[5], attribs[6])
                user.current_menu = None if attribs[-1].strip(
                ) == 'Nan' else attribs[-1].strip()
                users_db.add(user)


users_db = user_db.UserDB()
get_backuped_users()


@app.route("/")
def home():
    """
    Home page, renders basic front page
    """
    username = escape(session['username']) if 'username' in session else False
    if username:
        user_obj = users_db.get(username)
        calc = Calculator(user_obj.weight, user_obj.height, user_obj.age, user_obj.gender, user_obj.activity)
        return render_template("home.html", title='Home page', username=username, normas=[calc.calories_need(), calc.proteins_need(), calc.fats_need(), calc.carbohydrates_need()])
    return render_template("home.html", title='Home page', username=username, normas=[])


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
            return redirect(url_for('home'))
        else:
            return render_template("failure.html", message="Wrong password")
    except user_db.UserNotFound:
        return render_template("failure.html", message="No such user")


@app.route('/register', methods=['GET'])
def register_page():
    '''
    This is get page for registration which renders form for registration
    '''
    if 'username' not in session:
        return render_template('registration.html', user_data=[])
    else:
        return render_template("failure.html", message="Your are already logged in", username=escape(session['username']))


@app.route('/profile')
def profile():
    '''
    User profile page where user information is displayed and can be changed
    '''
    if 'username' in session:
        user_obj = users_db.get(escape(session['username']))
        age = user_obj.age
        height = user_obj.height
        weight = user_obj.weight
        act = user_obj.activity
        gender = user_obj.gender
        return render_template("profile.html", title='Profile', username=escape(session['username']), user_data=[age, height, weight, act, gender])
    return "You are not logged in"


@app.route('/logout')
def logout():
    '''
    Logout route to remove user from session
    '''
    # remove the username from the session if it's there
    session.pop('username', None)
    a.clear()
    menu_final.clear()
    return redirect(url_for('home'))


@app.route('/profile', methods=['POST'])
def profile_update():
    '''
    This route changes user profile
    '''
    if 'username' in session:
        login = escape(session['username'])
        user_obj = users_db.get(login)
        age = request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        gender = request.form.get("gender")
        act = request.form.get("comp_select")
        user_obj.set_characteristics(age, height, weight, gender, act)

        with open("users.csv", "r") as f:
            users_backup = f.readlines()
        with open("users.csv", "w") as f:
            for user in users_backup:
                if user.split(',')[0].strip() != login:
                    f.write(user)
        backup_user(user_obj.login, user_obj.password, height,
                    weight, age, gender, act, user_obj.current_menu)
        return render_template("profile.html", title='Profile', user_data=[age, height, weight, act, gender], username=login)


@app.route("/registration", methods=["POST"])
def infor_user():
    """
    To get data from user
    """
    if user.set_characteristics(age, height, weight, gender, act):
        try:
            users_db.add(user)
        except Exception as err:
            print(err)
            return render_template("failure.html", message="User already exists", username=False)
        backup_user(login, password, height, weight, age, gender, act, [])
    return user, password, age, height, weight, gender, act


@app.route("/registration/submitted", methods=["POST"])
def file_html():
    """
    To return already submitted page
    """
    login = request.form.get("login")
    password = request.form.get("password")
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    gender = request.form.get("gender")
    act = request.form.get("comp_select")
    user = user_work.User(login)

    try:
        user.set_characteristics(age, height, weight, gender, act)
        try:
            user.set_password(password)
            users_db.add(user)
            backup_user(login, password, height, weight, age, gender, act, [])
            return redirect(url_for('home', title='Home page', username=False))
        except user_work.PasswordTooShortError:
            return render_template("failure.html")
    except ValueError:
        return render_template("failure.html")

# MENU


class CurrentMenu:
    def __init__(self):
        self.cur_menu = None

    def set_men(self, menu):
        self.cur_menu = menu


db_dishes = []
menu_final = []
a = []


@app.route('/menu', methods=['post'])
def generate_menu_page():
    '''
    This route is used to calculated parameters and then create menu,
    which is then attached to user instance (new attribute).
    Clicking "Generate" button on base.html page redirects to this route.
    If no username in session, redirects to home page
    '''
    # menu_final.clear()
    if 'username' in session:
        menu_final.clear()
        user_obj = users_db.get(escape(session['username']))
        calc = Calculator(user_obj.weight, user_obj.height,
                          user_obj.age, user_obj.gender, user_obj.activity)
        menu = Menu(calc.calories_need(), calc.proteins_need(), calc.fats_need(),
                    calc.carbohydrates_need(), [])

        menu11 = Menu(calc.calories_need(), calc.proteins_need(), calc.fats_need(),
                      calc.carbohydrates_need(), [])
        menu11.generate_menu()

        dish = request.form.get("dish_change")
        menu.generate_menu()
        db_dishes.append(menu)
        if dish != 'all':
            menu_use = db_dishes[0]
        else:
            menu_use = db_dishes[-1]
        if dish != "None":
            if dish == 'first':
                menu_use.delete_dish(menu_use.menu[0])
                menu_use.generate_dish()
                # menu1 = menu.generate_menu()
                m1 = ''.join(str(menu_use).split('----------')[0])
                m2 = ''.join(str(menu_use).split('----------')[1])
                m3 = ''.join(str(menu_use).split('----------')[2])
                # user_obj.current_menu = [m1, m2, m3]
                user_obj.current_menu = [
                    menu_use.menu[0], menu_use.menu[1], menu_use.menu[2]]
                return render_template("base.html", username=escape(session['username']), title='Menu', menu1=m1, menu2=m2, menu3=m3)
            if dish == 'second':
                menu_use.delete_dish(menu_use.menu[1])
                menu_use.generate_dish()
                # menu1 = menu.generate_menu()
                m1 = ''.join(str(menu_use).split('----------')[0])
                m2 = ''.join(str(menu_use).split('----------')[1])
                m3 = ''.join(str(menu_use).split('----------')[2])
                user_obj.current_menu = [
                    menu_use.menu[0], menu_use.menu[1], menu_use.menu[2]]
                return render_template("base.html", username=escape(session['username']), title='Menu', menu1=m1, menu2=m2, menu3=m3)
            if dish == 'third':
                # menu1 = menu.generate_menu()
                menu_use.delete_dish(menu_use.menu[2])
                menu_use.generate_dish()
                m1 = ''.join(str(menu_use).split('----------')[0])
                m2 = ''.join(str(menu_use).split('----------')[1])
                m3 = ''.join(str(menu_use).split('----------')[2])
                # user_obj.current_menu = [m1, m2, m3]
                user_obj.current_menu = [
                    menu_use.menu[0], menu_use.menu[1], menu_use.menu[2]]
                return render_template("base.html", username=escape(session['username']), title='Menu', menu1=m1, menu2=m2, menu3=m3)

            else:
                menu_use.generate_menu()
                m1 = ''.join(str(menu_use).split('----------')[0])
                m2 = ''.join(str(menu_use).split('----------')[1])
                m3 = ''.join(str(menu_use).split('----------')[2])
                user_obj.current_menu = [
                    menu_use.menu[0], menu_use.menu[1], menu_use.menu[2]]
                # user_obj.current_menu = [m1, m2, m3]
                return render_template("base.html", username=escape(session['username']), title='Menu', menu1=m1, menu2=m2, menu3=m3)

            # where_next = request.form.get('choice')
        else:
            # if where_next != "Regenerate":
            # print(len(str(menu_use.menu).split('----------')[-3:]))
            # for i in str(menu_use.menu).split('----------')[-3:]:
            # print(len(menu_use.menu))
            menu_use.accept_dish(menu_use.menu[0])
            menu_use.accept_dish(menu_use.menu[2])
            menu_use.accept_dish(menu_use.menu[1])

            cal = menu_use.daily_calories
            prot = menu_use.daily_proteins
            fats = menu_use.daily_fats
            carb = menu_use.daily_carbohydrates
            lst_new = [cal, prot, fats, carb]
            a.append(lst_new)
            menu_final.clear()
            db_dishes.clear()
            menu_final.append(menu_use)

            return redirect(url_for('home', title='Home page', username=escape(session['username']), message='Added daily menu successfuly'))
            # return render_template("base.html", title='Menu', menu1=m1, menu2=m2, menu3=m3)
    else:
        return render_template("failure.html", message="Not logged in", username=False)

# a = []


@app.route('/menu', methods=['get'])
def get_menu_page():
    """
    This route renders base.html page with menu if it is generated or with single button to
    generate menu otherwise (watch base.html on the bottom)
    This route can not be accessed without being logged in, so sample page will be rendered
    if there is no username in session
    """
    if 'username' in session:
        user_obj = users_db.get(escape(session['username']))
        menu_res = False if not user_obj.current_menu else user_obj.current_menu
        # dish = request.form.get("dish_change")
        if menu_res:
            m1 = menu_res[0]
            m2 = menu_res[1]
            m3 = menu_res[2]
        else:
            m1 = []
            m2 = []
            m3 = []

        return render_template("base.html", username=escape(session['username']), title='Menu', menu1=m1, menu2=m2, menu3=m3)
    else:
        return "You are not logged in"


# @app.route('/menuopt', methods=['post'])
# def find_smth():
#     if 'username' in session:
#         return render_template('menuoptional.html')
#     else:
#         return "You are not logged in"

@app.route('/menuopt', methods=['GET'])
def menu():
    '''
    Get route for optional menu page: renders page with field to find custom food
    '''
    if 'username' in session:
        return render_template('menuoptional.html', username=escape(session['username']))
    else:
        return "Your are not logged in"


lyst = []


@app.route('/menuopt/subm', methods=['post'])
def add_cals1():
    '''
    Post route for optional menu. Adds custom product to products
    '''
    if 'username' in session:
        food = request.form.get("keyword")
        # food = own_menu()
        pr = Product(food)
        lst = pr.get_products()
        for i in lst:
            lyst.append(i)
        if len(lst) != 0:
            return render_template('productsearch.html', username=escape(session['username']), vars=lst)
        else:
            return render_template("failure.html")
    else:
        return render_template("failure.html")

# a = []


@app.route('/menuopt/subm/choice', methods=['GET'])
def all_of_them():
    '''
    Get route to render productsearch page
    '''
    if 'username' in session:
        return render_template('productsearch.html', username=escape(session['username']), vars=lyst)
    else:
        return "Your are not logged in"


@app.route('/menuopt/subm/choice', methods=['post'])
def add_cals():
    '''
    Post route for optional choice product. User's product he chose from dropdown box
    '''
    if 'username' in session:
        # lst =
        user_obj = users_db.get(escape(session['username']))
        calc = Calculator(user_obj.weight, user_obj.height, user_obj.age, user_obj.gender, user_obj.activity)
        food = request.form.get("menu")
        weight = request.form.get('keyword')
        pr = Product(food)
        # print(weight)
        try:
            weig = float(weight)
            lst_here = []
            # lst_here.append(food)
            nutr = pr.choose_product(food, weig)
            a.append(nutr)
            # print(lst_here)
            # print(a)
            # for i in range(len(a)):
            return render_template('home.html', username=escape(session['username']), normas=[calc.calories_need(), calc.proteins_need(), calc.fats_need(), calc.carbohydrates_need()], vars=nutr)
        except TypeError:
            return "Wrong weight"
    else:
        return "You are not logged in"
    # print(a)


@app.route('/final', methods=['get'])
def calc_last():
    '''
    Get route for final menu page. Renders page with dishes and estimates how many calories
    will user consume in general
    '''
    if 'username' in session:

        # print(len(menu_final[0]))
        # print(menu_final[0])

        user_obj = users_db.get(escape(session['username']))
        menu_res = False if not user_obj.current_menu else user_obj.current_menu

        cals = 0
        fats = 0
        prots = 0
        carbs = 0
        for i in a:
            cals += i[0]
            prots += i[1]
            fats += i[2]
            carbs += i[3]
        if menu_res:
            for dish in user_obj.current_menu:
                cals += dish.calories
                fats += dish.fats
                prots += dish.proteins
                carbs += dish.carbohydrates

            m1 = menu_res[0]
            m2 = menu_res[1]
            m3 = menu_res[2]
            # m1 = ''.join(str(menu_final[0]).split('----------')[0])
            # m2 = ''.join(str(menu_final[0]).split('----------')[1])
            # m3 = ''.join(str(menu_final[0]).split('----------')[2])
        else:
            m1 = []
            m2 = []
            m3 = []
        return render_template('dishtoday.html', username=escape(session['username']), menu1=m1, menu2=m2, menu3=m3, cal=cals, prot=prots, fats=fats, carbs=carbs)
    else:
        return "Your are not logged in"


# print(a)
if __name__ == "__main__":
    FLASK_DEBUG = 1
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
