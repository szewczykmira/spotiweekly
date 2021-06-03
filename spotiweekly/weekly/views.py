from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from spotiweekly.spotify.authorization_api import AuthorizationClient
from spotiweekly.spotify.exceptions import CodeNotProvided
from spotiweekly.spotify.utils import retrieve_code

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    client = AuthorizationClient(current_app.config)
    url = client.authorization_url()
    return redirect(url)


@weekly_bp.route("/callback")
def callback():
    try:
        code = retrieve_code(request.args)
        client = AuthorizationClient(current_app.config)
        token = client.get_access_token(code)
        session[current_app.config["COOKIE_NAME"]] = token
        return redirect(url_for("weekly.index"))
    except CodeNotProvided:
        return "Something went wrong"


@weekly_bp.route("/logout")
def logout():
    del session[current_app.config["COOKIE_NAME"]]
    return redirect(url_for("weekly.index"))
