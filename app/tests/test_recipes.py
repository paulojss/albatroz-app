"""
#app/tests/test_recipes.py

Author: Paulo Jorge

"""


import os
import unittest
from app import app, db

class ProjectTests(unittest.TestCase):
	
	############################
	#### setup and teardown ####
	############################
	
	#executed prior to each test
	def setUp(self):
		app.config['TESTING']=True
		app.config['WTF_CSRF_ENABLED']=False
		app.config['DEBUG']=False
		app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + \
			os.path.join(app.config['BASEDIR'], TEST_DB)
		self.app = app.test_client()
		db.create_all()

		self.assertEquals(app.debug, False)

	#executed after each test
	def tearDown(self):
		db.session.remove()
		db.drop_all()


	###############	
	#### tests ####
	###############

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertIn(b'Imagens', response.data)

	def test_main_page_query_results(self):
		response = self.app.get('/add', follow_redirects=True)
		self.assertIn(b'Adicionar nova imagem',response.data)

	


if __name__ == "__main__":
	unittest.main()
