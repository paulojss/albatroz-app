"""
#app/recipes/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

from flask import render_template, Blueprint
from app.models import Image


 	#################
	#### config  ####
	#################

api_blueprint = Blueprint('api',__name__, template_folder='templates')

	
	#################
	#### routes  ####
	#################


@api_blueprint.route('/ns/v1')
def full_data():
	all_data = Image.query.all()
	return render_template('images.html', images=all_data)
