"""
Website v0
"""
from flask import Flask, session, redirect, url_for, render_template, request
import user_work
import user_db
from markupsafe import escape
from calculator import Calculator
from menu import Menu

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def backup_user(login, password, height, weight, age, gender, activity, current_menu):
    with open('users.csv', 'a') as f_users:
        f_users.write(','.join([ login, password, height, weight, age, gender, activity, 'Nan' ]))
        f_users.write('\n')


def get_backuped_users():
    with open('users.csv', 'r') as f_users:
        for line in f_users:
            if line.strip():
                attribs = line.split(',')
                user = user_work.User(attribs[0])

                user.set_password(attribs[1])
                user.set_characteristics(attribs[4], attribs[2], attribs[3], attribs[5], attribs[6])
                user.current_menu = None if attribs[-1].strip() == 'Nan' else attribs[-1].strip()
                users_db.add(user)


users_db = user_db.UserDB()
get_backuped_users()



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
    backup_user(login, password, height, weight, age, gender, act, [])
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
            return redirect(url_for('home', title='Home page', message='Registered', username=False))
        except user_work.PasswordTooShortError:
            return render_template("failure.html")
    except ValueError:
        return render_template("failure.html")



# MENU
@app.route('/menu', methods=['post'])
def generate_menu_page():
    '''
    This route is used to calculated parameters and then create menu,
    which is then attached to user instance (new attribute).

    Clicking "Generate" button on base.html page redirects to this route.

    If no username in session, redirects to home page
    '''
    if 'username' in session:
        user_obj = users_db.get(escape(session['username']))
        calc = Calculator(user_obj.weight, user_obj.height, user_obj.age, user_obj.gender, user_obj.activity)
        menu = Menu(calc.calories_need(), calc.proteins_need(), calc.fats_need(),\
                    calc.carbohydrates_need(), [])
        menu.generate_menu()
        user_obj.set_current_menu(menu.menu)
        return render_template("base.html", title='Menu', menu=user_obj.current_menu)
    else:
        return redirect(url_for('home', title='Home page', message='Not logged in', username=False))


@app.route('/menu', methods=['get'])
def get_menu_page():
    '''
    This route renders base.html page with menu if it is generated or with single button to
    generate menu otherwise (watch base.html on the bottom)

    This route can not be accessed without being logged in, so sample page will be rendered
    if there is no username in session
    '''
    if 'username' in session:
        user_obj = users_db.get(escape(session['username']))
        menu_res = False if not user_obj.current_menu else user_obj.current_menu
        return render_template("base.html", title='Menu', menu=menu_res)
    else:
        return "You are not logged in"



if __name__ == "__main__":
    FLASK_DEBUG=1
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
