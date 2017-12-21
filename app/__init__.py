"""
#app/__ini__.py

Author: Paulo Jorge

"""


#################
#### imports ####
#################


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads


#################
#### config  ####
#################


app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)



# Configure the image uploading via flask-uploads
image = UploadSet('images', IMAGES)
configure_uploads(app, images)

#################
### blueprints ##
#################


from app.users.views import users_blueprint
from app.recipes.views import recipes_blueprint

#register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)