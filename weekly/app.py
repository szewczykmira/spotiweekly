from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    ctx = {"value": "Miguel"}
    return render_template("index.html", **ctx)
