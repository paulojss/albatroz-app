"""
#app/api/forms.py


"""


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images


class AddItemForm(FlaskForm):
	img_name = StringField('Nome da imagem', validators=[DataRequired()])
	img_description = StringField('Descricao', validators=[DataRequired()])
	img_file = FileField('Adicione um arquivo', validators=[FileRequired(), FileAllowed(images, 'Apenas imagens!')]) 