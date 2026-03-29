from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,  SubmitField 
from wtforms.validators import DataRequired

class ClienteForma(FlaskForm):
    id = hidden_field = IntegerField('Id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresía', validators=[DataRequired()])
    guardar = SubmitField('Guardar')