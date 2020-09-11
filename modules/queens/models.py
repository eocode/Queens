"""
Game Queens models
"""
from sqlalchemy import Column, Integer
from app.extensions import db
from sqlalchemy.types import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Simulation(db.Model):
    """Simulation model for n cases"""

    __tablename__ = "simulations"
    id = Column(Integer, primary_key=True, doc="It's the n board or queen")
    solutions = Column(Integer, doc="Number of solutions found")
    board = Column(Text)
    solved = relationship("Solution", back_populates="simulation")

    def __init__(self, id, board, solutions):
        self.id = id
        self.board = board
        self.solutions = solutions

    def __repr__(self):
        return "<msg %r>" % (str(self.n))


class Solution(db.Model):
    """Detail of solutions"""

    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True)
    simulation_id = Column(Integer, ForeignKey("simulations.id"))
    simulation = relationship("Simulation", back_populates="solved")
    solution = Column(Text, doc="Json with the solution")
    solution_number = Column(Integer, doc="Number of solution")

    def __init__(self, simulation_id, solution):
        self.simulation_id = simulation_id
        self.solution = solution

    def __repr__(self):
        return "<msg %r>" % (str(self.solution))
