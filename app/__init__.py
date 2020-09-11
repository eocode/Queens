"""
Initialized app
"""

from flask import Flask
from modules.queens.views import queens_view
from dotenv import load_dotenv
from app.extensions import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

load_dotenv(".env")


def create_app(test_config=None):
    """Basic modularized app configuration"""
    app = Flask(__name__)

    app.config.from_pyfile("settings_base.py")

    if test_config is None:
        app.config.from_pyfile("settings_prod.py")
    else:
        app.config.from_pyfile("settings_test.py")

    db.init_app(app)
    Bootstrap(app)
    with app.app_context():
        app.register_blueprint(queens_view)
        Migrate(app, db)

    return app


queen = create_app(test_config=True)
