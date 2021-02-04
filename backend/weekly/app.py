from flask import Flask
from flask_cors import CORS

from .config import Config
from .views import weekly_bp


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(weekly_bp)
    CORS(app)
    return app


app = create_app()
