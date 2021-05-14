"""
Home page
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home page
    """
    return render_template("home.html")


@app.route("/", methods=["POST"])
def login():
    """
    This is post request to home page
    """
    login = request.form.get("login")
    password = request.form.get("password")    
    # And then create user session
    return render_template("home.html")



if __name__ == "__main__":
    FLASK_DEBUG=1
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)

