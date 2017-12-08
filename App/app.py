"""
*
*
*
"""
from flask import Flask, jsonify
import random

from db import file
from motor import motor


app = Flask(__name__)
imagens = motor(file)

@app.route("/")
def json_api():
	
	
	print(imagens)

	#noticias = [{ "imagem" : img }]			
	
	return imagens=imagens
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

