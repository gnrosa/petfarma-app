from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class FormConsulta(FlaskForm):
	id = IntegerField('Número do pedido', validators=[DataRequired()])