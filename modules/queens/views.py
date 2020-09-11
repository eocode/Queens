from flask import Blueprint, render_template

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
    return render_template(
        "simulation.html", title="Queens", board={}, solutions={}, a=5
    )
