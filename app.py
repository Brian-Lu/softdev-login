from flask import Flask, render_template, request, session, redirect, url_for
from utils import register, login
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)
print app.secret_key
@app.route("/")
def index():
    if 'username' not in session:
        return render_template("login.html")
    else:
        return render_template("home.html", status = session["status"], user = session["username"])
@app.route("/authenticate", methods = ['POST', 'GET'])
def authenticate():
    if request.method == 'POST':
        if "register" in request.form:
            status = register.register(request.form["username"], request.form["password"])
            return render_template("login.html", status = status)
        elif "login" in request.form:
            session["status"] = login.login(request.form["username"], request.form["password"])
            return render_template("home.html", status = session["status"], user = session["username"])
        else:
            return "Sorry, there seems to be an error"
    elif request.method == 'GET':
        return "Please enter this URL through the root route form!!!"
@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('username')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
