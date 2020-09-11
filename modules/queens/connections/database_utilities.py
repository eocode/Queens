"""
Utility for set data on app
"""

from app.extensions import db
from modules.queens.models import Simulation, Solution


def create_or_update(instance, model):
    """Create or update if the data not exists"""
    if instance:
        if isinstance(model, Simulation):
            # Update
            instance.solutions = model.solutions
            instance.time_start = model.time_start
            instance.time_end = model.time_end
            instance.minutes = round(model.minutes, 3)
        else:
            instance.solution = model.solution
    else:
        # Create
        db.session.add(model)
    db.session.commit()

    return instance


def add(model):
    """Validate data for personalized query insert or update"""
    # Filter by id
    if isinstance(model, Simulation):
        instance = model.query.filter_by(id=model.id).first()
    # Personalized solutions filter
    else:
        instance = model.query.filter_by(
            simulation_id=model.simulation_id, solution_number=model.solution_number
        ).first()
    return create_or_update(instance=instance, model=model)


def get(model):
    """Validate data for personalized query insert or update"""
    # Filter by id
    if isinstance(model, Simulation):
        instance = model.query.filter_by(id=model.id).first()
    # Personalized filter
    else:
        instance = model.query.filter_by(
            simulation_id=model.simulation_id, solution_number=model.solution_number
        ).first()
    return instance
