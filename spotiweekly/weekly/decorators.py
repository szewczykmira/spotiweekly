from functools import wraps

from flask import current_app, session


def is_logged_in(view):
    @wraps(view)
    def inner(*args, **kwargs):
        ctx = {"is_authenticated": current_app.config["COOKIE_NAME"] in session}
        return view(ctx, *args, **kwargs)

    return inner
