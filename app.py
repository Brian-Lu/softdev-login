from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("login.html")
@app.route("/authenticate", methods = ['POST'])
def authenticate():
    if request.form['username'] == 'username' and request.form['password'] == 'password':
        return render_template("authenticate.html", status = "success")
    else:
        return render_template("authenticate.html", status = "failure")

if __name__ == "__main__":
    app.run()