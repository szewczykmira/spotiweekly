from flask import (
    Blueprint,
    current_app,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from spotiweekly.spotify.api import SpotifyClient
from spotiweekly.spotify.authorization_api import AuthorizationClient
from spotiweekly.spotify.exceptions import CodeNotProvided
from spotiweekly.spotify.utils import retrieve_code
from spotiweekly.weekly.decorators import is_logged_in

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
@is_logged_in
def index(ctx):
    return render_template("index.html", **ctx)


@weekly_bp.route("/playlists")
@is_logged_in
def playlists(ctx):
    offset = request.args.get("offset")
    if ctx["is_authenticated"]:
        token = session[current_app.config["COOKIE_NAME"]]
        client = SpotifyClient(token)
        response = client.all_playlists(offset)
        return jsonify(response)
    return 200, jsonify({"items": [], "previous": "", "next": ""})


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
    except CodeNotProvided as e:
        current_app.logger.exception(str(e))
        return "Something went wrong"


@weekly_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("weekly.index"))
