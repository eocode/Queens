"""Generate db instance for SQLAlchemy"""

from flask_sqlalchemy import SQLAlchemy
from .database import metadata

db = SQLAlchemy(metadata=metadata)
