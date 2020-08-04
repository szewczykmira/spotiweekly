from flask import Flask

from .config import Config
from .views import weekly_bp


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(weekly_bp)
    return app


app = create_app()
