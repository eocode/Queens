from flask import Blueprint, render_template, redirect
from .forms import SimulateForm
from modules.queens.algorithms.nqueens import NQueens
from modules.queens.utilities.json_array_operations import convert_json_in_array
from modules.queens.models import Simulation

queens_view = Blueprint(
    "queens",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)


@queens_view.route("/", methods=["GET"])
def queens_app():
    form = SimulateForm()
    return render_template("index.html", title="Queens", form=form)


@queens_view.route("/simulation", methods=["POST", "GET"])
def queens_simulation():
    form = SimulateForm()
    if form.validate_on_submit():
        simulate = NQueens(n=form.n.data, persistence=True)
        print(form.repeat.data)
        if not simulate.is_solved() or form.repeat.data:
            simulate.solve()

        solutions = {}
        pages = simulate.get_solutions(form.page.data)
        for s in pages.items:
            solutions[s.solution_number] = convert_json_in_array(s.solution)

        return render_template(
            "simulation.html",
            title="Queens",
            board={},
            solutions=solutions,
            form=form,
            a=form.n.data,
            has_next=pages.has_next,
            has_prev=pages.has_prev,
            prev_num=pages.prev_num,
            next_num=pages.next_num,
            total=pages.total,
        )
    return redirect("/")


@queens_view.route("/boards", methods=["GET"])
def queens_board():
    form = SimulateForm()
    boards = Simulation.query.order_by(Simulation.id.asc()).all()
    return render_template("boards.html", title="Queens", boards=boards, form=form)
