"""
app/recipes/views.py

Author:Paulo Jorge


"""
	#################
	#### imports ####
	#################

from flask import render_template, Blueprint


 	#################
	#### config  ####
	#################

recipes_blueprint = Blueprint('recipes',__name__, template_folder='templates')
	
	
	#################
	#### routes  ####
	#################


@recipes_blueprint.route('/ns/v1', methods=['GET'])
def full_data():
	return render_template('index.html')
