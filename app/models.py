"""
#app/models.py

Author: Paulo Jorge


"""


from app import db


class Image(db.Model):
	__tablename__ = "propagand"

	id = db.Column(db.Integer, primary_key=True)
	file_description = db.Column(db.String, nullable=False)
	file_name = db.Column(db.String, nullable=False)
	#img_url  = db.Column(db.String, nullable=False)

	def __init__(self, name, description):
		self.file_name = name
		self.file_description = description
		#self.img_url  = url


	def __repr__(self):
		return '<id: {}, title: {}>'.format(self.id,self.name)
