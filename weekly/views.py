from flask import Blueprint, render_template

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    return "Authenticate"
