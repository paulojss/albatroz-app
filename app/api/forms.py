"""
#app/api/forms.py


"""


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddItemForm(Form):
	img_title = StringField('Nome da imagem', validators=[DataRequired()])
	img_description = StringField('Descricao', validators=[DataRequired()])