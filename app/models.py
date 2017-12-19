"""
#app/models.py

Author: Paulo Jorge


"""


from app import db


class Recipe(db.Model):
	__tablename__ = "propaganda"

	id = db.Column(db.Integer, primary_key=True)
	file_description = db.Column(db.String, nullable=False)

	def __init__(self, description):
		self.file_description = description

	def __repr__(self):
		return '<title {}'.format(self.name)
