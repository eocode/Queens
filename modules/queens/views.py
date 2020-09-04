from flask import Blueprint, render_template, abort
from .utilities.json_array_operations import convert_array_in_json
from .algorithms.queens import Queens
from .models import Game
from .connections.CRUD import create_or_update

queens_view = Blueprint('queens',
                        __name__,
                        url_prefix='/',
                        template_folder='templates',
                        static_folder='static')


@queens_view.route("/")
def queens_app():
    # abort(404)
    return render_template('index.html', title='Queens')


@queens_view.route("/tests")
def tests_app():
    n = 8
    player = Queens(n)
    player.create_board()
    player.print_board()
    a = player.get_board()

    b = convert_array_in_json(a)
    player = Game(n, b, 3)
    create_or_update(player)

    print(b)

    return render_template('solution.html', title='Queens', board=a)


@queens_view.route("/test")
def test_app():
    game = Game.query.filter_by(id=8).first()
    player = Game(8, game.board, 6)
    player = create_or_update(player)

    return render_template('solution.html', title='Queens', board=player.solutions)
