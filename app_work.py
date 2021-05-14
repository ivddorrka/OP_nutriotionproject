"""
Website v0
"""
from flask import Flask, redirect, url_for, render_template, request
import user_work

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home page
    """
    return render_template("home.html", title='Home page')


@app.route("/", methods=["POST"])
def login():
    """
    This is post request to home page
    """
    login = request.form.get("login")
    password = request.form.get("password")    
    # And then create user session
    return render_template("home.html")


@app.route('/register', methods=['GET'])
def register_page():
    return render_template("registration.html", title='Register')



@app.route('/profile')
def profile():
    return render_template("profile.html", title='Profile')

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
            return render_template("calc.html")
        except user_work.PasswordTooShortError:
            return render_template("failure.html")
    except ValueError:
        return render_template("failure.html")


if __name__ == "__main__":
    FLASK_DEBUG=1
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)

