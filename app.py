from flask import Flask, render_template, request
from utils import register, login
import os
app = Flask(__name__)
app.secret_key = os.urandom(32
print app.secret_key
@app.route("/")
def index():
    return render_template("login.html")
@app.route("/authenticate", methods = ['POST'])
def authenticate():
    if "register" in request.form:
        status = register.register(request.form["username"], request.form["password"])
        return render_template("login.html", status = status)
    elif "login" in request.form:
        status = login.login(request.form["username"], request.form["password"])
        return render_template("authenticate.html", status = status)
    else:
        return "Sorry, there seems to be an error"

if __name__ == "__main__":
    app.run()
