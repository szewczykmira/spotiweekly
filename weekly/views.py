from flask import Blueprint, current_app, redirect, render_template, request, session
from spotify.api import get_auth_url
from spotify.exceptions import CodeNotProvided
from spotify.utils import retrieve_code

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    auth_url = get_auth_url(current_app.config)
    return redirect(auth_url)


@weekly_bp.route("/callback")
def callback():
    try:
        return retrieve_code(request.args)
    except CodeNotProvided:
        return "Something went wrong"
