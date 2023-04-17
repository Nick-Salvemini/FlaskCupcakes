from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, URLField
from wtforms.validators import NumberRange

class AddCupcakeForm(FlaskForm):

    flavor = StringField('Flavor')
    size = SelectField('Size', choices=['Small', 'Medium', 'Large'])
    rating = FloatField('Rating', NumberRange(min=0, max=10))
    image = URLField('Image')