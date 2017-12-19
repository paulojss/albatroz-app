"""
#app/tests/test_recipes.py

Author: Paulo Jorge

"""

import unittest
from app import app

class ProjectTests(unittest.TestCase):
	
	############################
	#### setup and teardown ####
	############################
	
	#executed prior to each test
	def setUp(self):
		app.config['TESTING']=True
		app.config['DEBUG']=False
		self.app = app.test_client()

		self.assertEquals(app.debug, False)

	#executed after each test
	def tearDown(self):
		pass

	###############	
	#### tests ####
	###############

	def test_main_page(self):
		response = self.app.get('/ns/v1', follow_redirects=True)
<<<<<<< HEAD
		self.assertI(b'
=======
		self.assertIn(b'FULL DATA', response.data)


if __name__ == "__main__":
	unittest.main()
>>>>>>> add_blueprints
