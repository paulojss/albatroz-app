"""
#app/recipes/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

from flask import render_template, Blueprint, request

from app.models import Image
from .forms import AddItemForm


 	#################
	#### config  ####
	#################

api_blueprint = Blueprint('api',__name__, template_folder='templates')

	
	#################
	#### routes  ####
	#################


@api_blueprint.route('/')
def full_data():
	all_data = Image.query.all()
	return render_template('images.html', images=all_data)


@api_blueprint.route('/add', methods=['GET','POST'])
def add_img():
	form = AddItemForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_img = Image(form.img_title.data, form.img_description.data)
			db.session(new_img)
			db.session.commit()
			flash('New image, {}, added!'.format(new_img.img_title), 'success')
			return redirect(url_for('api.index'))
		else:
			flash_errors(form)
			flash('ERROR! Image was not added.', 'error')
	return render_template('add_img.html', form=form)







