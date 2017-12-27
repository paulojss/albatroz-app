"""
#app/users/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from flask_admin.helpers import flash_errors

from app import db
from app.models import User
from app.users.forms import RegisterForm

	#################
	#### config  ####
	#################

users_blueprint = Blueprint('users',__name__)


	#################
	#### routes  ####
	#################


@users_blueprint.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
				new_user.authenticated = True
				db.session.add(new_user)
				db.session.commit()
				flash('Registrado com sucesso!','success')
				return redirect(url_for('api.index'))
			except IntegrityError:
				db.session.rollback()
				flash('Email "{}" ja existe!'.format(form.email.data), 'error')	
	return render_template('register.html', form=form)
