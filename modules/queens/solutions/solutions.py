"""
Save solutions in PostgreSQL to
"""

import copy
from ..models import Simulation
from ..connections.database_utilities import add, get
from ..utilities.json_array_operations import convert_array_in_json
from sqlalchemy.orm import load_only
from ..models import Solution
from datetime import datetime


class Solutions:
    """Save all solutions generated for the algorithm"""

    def __init__(self, n, persistence=False):
        self.__n = n
        self.__solutions = {}
        self.__num_solutions = 0
        # Enable save on PostgreSQL
        self.__persistence = persistence
        # For time control
        self.__elapsed_time = 0.0
        self.__limit_of_minutes = 10
        self.__continue = True
        self.__time_start = datetime.now()
        self.__time_end = datetime.now()
        # Get solutions
        self.__per_page = 10

    def validate_if_continue(self):
        """If continue status change and stop with false"""
        return self.__continue

    def is_valid_in_range_of_minutes(self):
        """Verify if solutions are in range of minutes
        if false stop app and show results
        """
        time_delta = (self.__time_end - self.__time_start).total_seconds()
        self.__elapsed_time = time_delta / 60
        if self.__elapsed_time > self.__limit_of_minutes:
            self.__continue = False
        else:
            self.__continue = True

    def update_simulation(self):
        """Update simulation for n*n
        If exists only will update set in 0s
        On finish will update with last data
        """
        if self.__persistence:
            simulation = Simulation(
                id=self.__n,
                solutions=self.__num_solutions,
                time_start=self.__time_start,
                time_end=self.__time_end,
                minutes=self.__elapsed_time,
            )
            return add(simulation)
        return None

    def add_solution(self, board):
        """Add a solution"""
        self.__num_solutions += 1
        if self.__persistence:
            json_board = convert_array_in_json(board)
            save_solution = Solution(
                simulation_id=self.__n,
                solution=json_board,
                solution_number=self.__num_solutions,
            )
            add(model=save_solution)
        else:
            self.__solutions[self.__num_solutions] = copy.copy(board)
        self.__time_end = datetime.now()
        self.is_valid_in_range_of_minutes()
        self.update_simulation()
        return True

    def get_solution(self, value):
        """Get a specific solution"""
        if self.__persistence:
            get_solution = Solution(
                simulation_id=self.__n, solution=None, solution_number=value
            )
            return get(get_solution)
        else:
            return self.__solutions[value]

    def get_solutions(self, page):
        """Return all solutions"""
        if self.__persistence:
            return (
                Solution.query.filter_by(simulation_id=self.__n)
                .options(load_only("solution", "solution_number"))
                .order_by(Solution.id.asc())
                .paginate(page, self.__per_page, error_out=False)
            )
        else:
            return self.__solutions
