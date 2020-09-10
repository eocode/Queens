from flask import Blueprint, render_template
from .simulation.simulation import Simulation
from .models import Game
from .connections.CRUD import create_or_update

queens_view = Blueprint(
    "queens",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)


@queens_view.route("/")
def queens_app():
    return render_template("index.html", title="Queens")


@queens_view.route("/simulation")
def simulation_app():
    n = 4
    player = Simulation(n)
    player.start()
    board = player.get_board()
    solutions = player.get_solutions()
    a = player.a

    return render_template("simulation.html", title="Queens", board=board, solutions=solutions, a=a)


@queens_view.route("/test")
def test_app():
    game = Game.query.filter_by(id=8).first()
    player = Game(8, game.board, 6)
    player = create_or_update(player)

    return render_template("simulation.html", title="Queens", board=player.solutions)
