"""
Initialized app
"""

from flask import Flask
from modules.queens.views import queens_view
from dotenv import load_dotenv
from .extensions import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

load_dotenv(".env")


def create_app(test_config=None):
    """Basic modularized app configuration"""
    app = Flask(__name__)

    app.config.from_pyfile("settings_base.py")

    print("test_config")
    print(test_config)
    if test_config is False:
        app.config.from_pyfile("settings_prod.py")
    else:
        print("Testing")
        app.config.from_pyfile("settings_test.py")

    db.init_app(app)
    Bootstrap(app)
    with app.app_context():
        app.register_blueprint(queens_view)
        Migrate(app, db)

    return app
