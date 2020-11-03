from flask import Flask, render_template, request, redirect, url_for, session
import mongo


app = Flask(__name__, static_url_path="/static")
app.debug = True
app.secret_key = 'Nothing'


@app.route("/")
def LoginPage():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
