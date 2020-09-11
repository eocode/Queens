from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class SimulateForm(FlaskForm):
    n = IntegerField('Choise n value to simulate board and get all solutions', validators=[DataRequired()])
    submit = SubmitField('Simulate board')
