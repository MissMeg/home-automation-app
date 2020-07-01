# flask info for the todo item and grocery item forms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class GroceryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    description = TextAreaField(
        'Description',
        validators=[DataRequired()]
    )


class TodoForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired()]
    )
    location = StringField(
        'Location',
        validators=[DataRequired()]
    )