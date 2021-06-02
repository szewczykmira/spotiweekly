from flask import Blueprint, current_app, redirect, request
from spotiweekly.spotify.authorization_api import AuthorizationClient
from spotiweekly.spotify.exceptions import CodeNotProvided
from spotiweekly.spotify.utils import retrieve_code
from spotiweekly.weekly.helpers import get_callback_url

weekly_bp = Blueprint("weekly", __name__)


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
        return redirect(get_callback_url(current_app.config, token))
    except CodeNotProvided:
        return "Something went wrong"
