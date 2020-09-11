"""
Utility for set data on app
"""

from app.extensions import db


def create_or_update(model):
    """Create or update if the data not exists"""
    instance = model.query.filter_by(id=model.id).first()
    if instance:
        # Update
        instance.board = model.board
        instance.solutions = model.solutions
    else:
        # Create
        db.session.add(model)
    db.session.commit()

    return instance
