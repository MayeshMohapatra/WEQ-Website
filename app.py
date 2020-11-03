from flask import Flask, render_template, request, redirect, url_for, session
import mongo

app = Flask(__name__)
app.debug = True
app.secret_key = 'Nothing'


@app.route("/login")
def LoginPage():
    return render_template("Signin.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
