from flask import Blueprint, current_app, redirect, render_template, request
from spotify.client import SpotifyAuthenticationClient

weekly_bp = Blueprint("weekly", __name__)


@weekly_bp.route("/")
def index():
    return render_template("index.html")


@weekly_bp.route("/authenticate")
def authenticate():
    client = SpotifyAuthenticationClient(current_app.config)
    return redirect(client.auth_url)


@weekly_bp.route("/callback")
def callback():
    print(request.data)
    return request.data
