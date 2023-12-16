from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddCupcakeForm(FlaskForm):
    flavor = StringField('Flavor',
                         validators=[InputRequired()])
    
    size = StringField('Size',
                     validators=[InputRequired()])
    
    rating = IntegerField('Rating',
                        validators=[InputRequired(),
                                    NumberRange(min=0, max=10)])
    
    image = URLField('Image URL',
                   validators=[Optional()])