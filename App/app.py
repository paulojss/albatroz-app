"""
*
*
*
"""
<<<<<<< HEAD
from flask import Flask, jsonify,url_for
=======
from flask import Flask, jsonify, url_for, render_template
>>>>>>> a3e95c3926703073c36dbbcd80bf8e07cde73dd2
import random
import os

from db import file
from motor import motor


app = Flask(__name__)
imagens = motor(file)



@app.route("/v1",methods=['GET'])
def json_api():
<<<<<<< HEAD
	
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
=======
	img = '/static/img/640full-amanda-lee-(i).jpg'
	img2 = 'http://localhost:5000'+img
	imagem =[{'img': img2}]
	#return render_template('index.html') 
	#return '<img src='+img+' />'
	return jsonify(imagem=imagem)

>>>>>>> a3e95c3926703073c36dbbcd80bf8e07cde73dd2

@app.route("/img/m")
def json_img():
	img = '../static/img/640full-amanda-lee-(i).jpg'
	
	#return render_template('index.html') 
	return '<img src='+img+' />'
	#return jsonify(imagem=imagem)

	
app.run(debug=True)

