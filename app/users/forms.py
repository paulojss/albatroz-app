"""
#app/users/forms.py


"""


from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(Form):
	first_name = StringField('Nome', validators=[DataRequired(), Length(min=3, max=40)])
	last_name = StringField('Sobrenome', validators=[DataRequired(), Length(min=3, max=40)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
	password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=40)])
	confirm = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('password')])
