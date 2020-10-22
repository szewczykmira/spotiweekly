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
from spotify.api import SpotifyClient
from spotify.authorization_api import AuthorizationClient
from spotify.consts import SPOTIFY_COOKIE_NAME
from spotify.exceptions import CodeNotProvided
from spotify.utils import retrieve_code

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    session_token = session.get(SPOTIFY_COOKIE_NAME)
    if session_token is not None:
        client = SpotifyClient(session_token)
        return render_template("index.html", **client.me().json())
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    client = AuthorizationClient(current_app.config)
    return redirect(client.authorization_url())


@weekly_bp.route("/callback")
def callback():
    try:
        code = retrieve_code(request.args)
        client = AuthorizationClient(current_app.config)
        response = make_response(redirect(url_for("weekly.index")))
        session[SPOTIFY_COOKIE_NAME] = client.get_access_token(code)
        response.headers["Same-Site"] = None
        return response
    except CodeNotProvided:
        return "Something went wrong"


@weekly_bp.route("/logout")
def logout():
    session.pop(SPOTIFY_COOKIE_NAME)
    return redirect(url_for("weekly.index"))
