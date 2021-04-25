from flask import Flask, redirect, url_for, render_template, request
from PY_files import user_work

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home page
    """
    return render_template("registration.html")

# @app.route("/registration", methods=["POST"])
# def register():
#     """
#     To get data from user
#     """
#     login = request.form.get("login")
#     password = request.form.get("password")
#     # redirect(url_for('questions'))
#     return user_work.User(login, password)



@app.route("/registration", methods=["POST"])
def infor_user():
    """
    To get data from user
    """
    # render_template("index.html")
    login = request.form.get("login")
    password = request.form.get("password")    
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    gender = request.form.get("gender")
    act = request.form.get("comp_select")
    user = user_work.User(login, password)
    return user, age, height, weight, gender, act


@app.route("/registration/submitted", methods=["POST"])
def file_html():
    """
    To return already submitted page
    """
    # user = register()
    info = infor_user()
    user = info[0]
    age = info[1]
    height = info[2]
    weight = info[3]
    gender = info[4]
    act = info[5]

    try:
        user.set_characteristics(age, height, weight, gender, act)
        return render_template("calc.html")
    except ValueError:
        return render_template("failure.html")
    

if __name__ == "__main__":
    app.run(debug=False)