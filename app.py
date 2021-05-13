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


if __name__ == "__main__":
    app.run(debug=False)

