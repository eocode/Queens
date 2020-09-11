from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class SimulateForm(FlaskForm):
    n = IntegerField(
        "Choise n value to simulate board and get all solutions (in max 10m)",
        validators=[DataRequired()],
    )
    page = IntegerField(
        "Show boards by page number",
        validators=[DataRequired()],
    )
    repeat = IntegerField("Repeat board generation")
    submit = SubmitField("Simulate board")
