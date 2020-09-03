from app.extensions import db
from sqlalchemy.sql import insert, table
from sqlalchemy.orm import sessionmaker


def create_or_update(model):
    instance = model.query.filter_by(id=model.id).first()
    if instance:
        instance.board = model.board
        instance.solutions = model.solutions
    else:
        db.session.add(model)
    db.session.commit()
