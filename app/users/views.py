"""
#app/users/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

from flask import Blueprint, render_template, request

from app import db

	#################
	#### config  ####
	#################

users_blueprint = Blueprint('users',__name__, template_folder='templates')


	#################
	#### routes  ####
	#################


@users_blueprint.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form_validate_on_submit():
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
