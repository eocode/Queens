"""
Settings for a production/development env
"""
from os import environ

SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"
