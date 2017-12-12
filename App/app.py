"""
*
*
*
"""
from flask import Flask, jsonify, url_for, render_template
import random
import os

from db import file
from motor import motor


app = Flask(__name__)
imagens = motor(file)



@app.route("/v1",methods=['GET'])
def json_api():
	img = '/static/img/640full-amanda-lee-(i).jpg'
	img2 = 'http://localhost:5000'+img
	imagem =[{'img': img2}]
	#return render_template('index.html') 
	#return '<img src='+img+' />'
	return jsonify(imagem=imagem)


@app.route("/img/m")
def json_img():
	img = '../static/img/640full-amanda-lee-(i).jpg'
	
	#return render_template('index.html') 
	#return '<img src='+img+' />'
	#return jsonify(imagem=imagem)

	
app.run(debug=True)

