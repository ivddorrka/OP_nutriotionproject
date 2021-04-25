from flask import Flask, redirect, url_for, render_template, request
from PY_files import user_work

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home page
    """
    return render_template("index.html")

@app.route("/questions", methods=["POST"])
def register():
    """
    To get data from user
    """
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    gender = request.form.get("gender")
    act = request.form.get("comp_select")
    user = user_work.User(age,height, weight, gender,act)
    return user


@app.route("/questions/submitted", methods=["POST"])
def file_html():
    """
    To return already submitted page
    """
    user = register()
    try:
        user.set_characteristics()
        return render_template("calc.html")
    except ValueError:
        return render_template("failure.html")
    

if __name__ == "__main__":
    app.run(debug=False)