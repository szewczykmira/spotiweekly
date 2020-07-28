from flask import Flask

from .views import weekly_views

app = Flask(__name__)
app.register_blueprint(weekly_views)
