from flask import Blueprint, current_app, make_response, redirect, render_template, request
from spotify.api import get_auth_url
from spotify.consts import SPOTIFY_COOKIE_NAME
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
        code = retrieve_code(request.args)
        response = make_response(code)
        response.set_cookie(SPOTIFY_COOKIE_NAME, code)
        return response
    except CodeNotProvided:
        return "Something went wrong"


@weekly_bp.route("/logout")
def logout():
    response = make_response("You have been logout")
    response.set_cookie(SPOTIFY_COOKIE_NAME, "", max_age=0)
    return response
