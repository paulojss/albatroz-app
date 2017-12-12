"""
*
*
*
"""
from flask import Flask, jsonify,url_for
import random
import os

from db import file
from motor import motor


app = Flask(__name__)
imagens = motor(file)

@app.route("/")
def json_api():
	
	imagem = '<img src="albatroz-app/App/640full-amanda-lee-(i).jpg" />'
	filename = os.listdir('../static/img')
	print(imagem)

	#noticias = [{ "imagem" : img }]			
	
	return u'<img src='+filename[0]+'/>'
	'''
	<html>
		<head>
			<title>Spotipo</title>
		</head>
		<body>
			<img src=%s />
		</body>
	</html>
	''' 
	#return jsonify(noticias=noticias)


app.run(debug=True)

