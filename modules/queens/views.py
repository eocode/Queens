from flask import Blueprint, render_template, redirect
from .forms import SimulateForm
from modules.queens.algorithms.nqueens import NQueens

queens_view = Blueprint(
    "queens",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)


@queens_view.route("/", methods=['GET'])
def queens_app():
    form = SimulateForm()
    return render_template("index.html", title="Queens", form=form)


@queens_view.route("/simulation", methods=['POST'])
def simulation_app():
    form = SimulateForm()
    if form.validate_on_submit():
        simulate = NQueens(form.n.data)
        simulate.solve()
        return render_template(
            "simulation.html", title="Queens", board={}, solutions=simulate.get_solutions(), a=form.n.data
        )
    return redirect('/')
