from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, URLField
from wtforms.validators import NumberRange

class AddCupcakeForm(FlaskForm):

    flavor = StringField('Flavor')
    size = SelectField('Size', choices=['Small', 'Medium', 'Large'])
    rating = FloatField('Rating')
    image = URLField('Image')