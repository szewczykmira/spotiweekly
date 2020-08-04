from flask import Blueprint, current_app, redirect, render_template, request
from spotify.api import get_auth_url

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    auth_url = get_auth_url(current_app.config)
    print(auth_url)
    return redirect(auth_url)


@weekly_bp.route("/callback")
def callback():
    print(request.data)
    return request.data
