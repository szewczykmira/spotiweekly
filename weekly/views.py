from flask import (
    Blueprint,
    current_app,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
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
        session[SPOTIFY_COOKIE_NAME] = code
        response.headers["Same-Site"] = None
        return redirect(url_for("weekly.index"))
    except CodeNotProvided:
        return "Something went wrong"


@weekly_bp.route("/logout")
def logout():
    session.pop(SPOTIFY_COOKIE_NAME)
    return "You have been logut"
