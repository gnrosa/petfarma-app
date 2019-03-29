from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired

class FormConsulta(FlaskForm):
	id = IntegerField('Número do pedido', validators=[DataRequired()])

class LoginForm(FlaskForm):
	username = StringField('Usuário', validators=[DataRequired()])
	password = PasswordField('Senha', validators=[DataRequired()])