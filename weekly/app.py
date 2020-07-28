from flask import Flask

from .config import Config
from .views import weekly_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(weekly_bp)
