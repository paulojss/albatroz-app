"""
#app/recipes/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

import json
from random import randint
from flask import render_template, Blueprint, request, flash, redirect, url_for, jsonify
from flask_admin.helpers import flash_errors


from app import images, db
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
	form = AddItemForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			filename = images.save(request.files['img_file'])
			url = images.url(filename)
			new_img = Image(form.img_name.data, filename, form.img_description.data, url)
			db.session.add(new_img)
			db.session.commit()
			flash('New image, {}, added!'.format(new_img.img_name), 'success')
			return redirect(url_for('api.detail'))
		else:
			flash_errors(form)
			flash('ERROR! Image was not added.', 'error')
	return render_template('add_img.html', form=form)

@api_blueprint.route('/detail')
def detail():
	all_data = Image.query.all()
	return render_template('images.html', images=all_data)


@api_blueprint.route('/ns/v1')
def api_img():
	all_data = Image.query.all()
	c = len(all_data)# 'c' recebe a quantidade de url na base de dados
	n = randint(0, c-1)# 'n' recebe um numero aleatorio
	url = str(all_data[n])
	
	url_img = [
	{ 'url': url },
	{' count': n }]
	
	#return jsonify(url_img=url_img)
	return jsonify({'url': url})









