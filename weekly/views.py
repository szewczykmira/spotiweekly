from flask import Blueprint, render_template

weekly_views = Blueprint("weekly", __name__)


@weekly_views.route("/")
def index():
    ctx = {"value": "Miguel"}
    return render_template("index.html", **ctx)
