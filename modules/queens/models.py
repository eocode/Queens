"""
Game Queens models
"""
from sqlalchemy import Column, Integer, DateTime, Float
from app.extensions import db
from sqlalchemy.types import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Simulation(db.Model):
    """Simulation model for n cases"""

    __tablename__ = "simulations"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, doc="It's the n board or queen")
    solutions = Column(Integer, doc="Number of solutions found", nullable=False)
    solved = relationship("Solution", back_populates="simulation")
    time_start = db.Column(DateTime, doc="Set start time", nullable=True)
    time_end = db.Column(DateTime, doc="Set end time", nullable=True)
    minutes = db.Column(Float, doc="Set time in minutes", nullable=True)
    created_on = db.Column(DateTime, server_default=db.func.now())
    updated_on = db.Column(
        DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, id, solutions, time_start, time_end, minutes):
        self.id = id
        self.solutions = solutions
        self.time_start = time_start
        self.time_end = time_end
        self.minutes = minutes

    def __repr__(self):
        return str(self.n)


class Solution(db.Model):
    """Detail of solutions"""

    __tablename__ = "solutions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    simulation_id = Column(Integer, ForeignKey("simulations.id"))
    simulation = relationship("Simulation", back_populates="solved")
    solution = Column(Text, doc="Json with the solution")
    solution_number = Column(Integer, doc="Number of solution")
    created_on = db.Column(DateTime, server_default=db.func.now())
    updated_on = db.Column(
        DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, simulation_id, solution, solution_number):
        self.simulation_id = simulation_id
        self.solution = solution
        self.solution_number = solution_number

    def __repr__(self):
        return str(self.solution)
