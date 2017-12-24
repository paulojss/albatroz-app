"""
#app/models.py

Author: Paulo Jorge


"""


from app import db


class Image(db.Model):
	__tablename__ = "images"

	id = db.Column(db.Integer, primary_key=True)
	#user_id = db.Column(db.Integer, db.ForeignKey(users.id))
	img_name = db.Column(db.String, nullable=False)
	filename = db.Column(db.String, default=None, nullable=True)
	img_description = db.Column(db.String, nullable=False)
	img_url  = db.Column(db.String, default=None, nullable=False)

	def __init__(self, name, filename, description, url):
		self.img_name = name
		self.filename = filename
		self.img_description = description
		self.img_url = url


	def __repr__(self):
		return '{}'.format(self.img_url)
