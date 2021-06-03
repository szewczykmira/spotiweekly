from functools import wraps

from flask import current_app, session


def is_logged_in(view):
    @wraps(view)
    def inner(*args, **kwargs):
        ctx = dict()
        if current_app.config["COOKIE_NAME"] in session:
            ctx["is_authenticated"] = True
        return view(ctx, *args, **kwargs)

    return inner
