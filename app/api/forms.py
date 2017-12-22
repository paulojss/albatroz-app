"""
#app/api/forms.py


"""


from flask_wtf import Form as FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddItemForm(FlaskForm):
	img_title = StringField('Nome da imagem', validators=[DataRequired()])
	img_description = StringField('Descricao', validators=[DataRequired()])