from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    opening = StringField('Open Time', validators=[DataRequired()])
    closing = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee Rating',
        choices=[
            '',
            '✘',
            '☕️',
            '☕️☕️',
            '☕️☕️☕️',
            '☕️☕️☕️☕️',
            '☕️☕️☕️☕️☕️'
        ],
        validators=[DataRequired()],
        validate_choice=False
    )
    wifi_rating = SelectField(
        'Wifi Rating',
        choices=[
            '',
            '✘',
            '💪',
            '💪💪',
            '💪💪💪',
            '💪💪💪💪',
            '💪💪💪💪💪'
        ],
        validators=[DataRequired()],
        validate_choice=False
    )
    power_rating = SelectField(
        'Power Outlet Rating',
        choices=[
            '',
            '✘',
            '🔌',
            '🔌🔌',
            '🔌🔌🔌',
            '🔌🔌🔌🔌',
            '🔌🔌🔌🔌🔌'
        ],
        validators=[DataRequired()],
        validate_choice=False
    )
    submit = SubmitField('Submit')
