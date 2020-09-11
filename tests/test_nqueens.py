"""
Test nqueens algorithm
"""
from modules.queens.algorithms.nqueens import NQueens
from . import app

# n	solutions
# 1	1
# 2	0
# 3	0
# 4	2
# 5	10
# 6	4
# 7	40
# 8	92
# 9	352
# 10 724
# 11 2,680
# 12 14,200
# 13 73,712
# 14 365,596
# 15 2,279,184

"""Set the N size board"""
n = 10
solutions = 724


def test_n_queens(app):
    """Test main route of project"""
    simulate = NQueens(n, False)
    simulate.solve()
    assert len(simulate.get_solutions(1)) == solutions
    assert simulate.is_solved()


def test_n_queens_with_persistence(app):
    """Test main route of project"""
    with app.test_request_context("/"):
        simulate = NQueens(n, True)
        assert simulate.solve() is None
        assert len(simulate.get_solutions(1).items) > 0
        assert simulate.is_solved()
