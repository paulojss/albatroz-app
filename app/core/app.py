"""
*
*
*
"""
from flask import Flask, jsonify, url_for, render_template
from random import randint
import os

from run import app
from .db import ready_database


app = Flask(__name__)

file = ready_database()
list_imagens = motor(file)
url_img = ''

IMG_DIR = '/static/img/'
URL_BASE = 'http://localhost:5000'

@app.route("/ns/v1",methods=['GET'])
def json_api():
	#length = len(list_imagens)
	#print (randint(0,length))
	#print ('length ',length)
	#print(list_imagens)

	#Retira o espaco em vazio da lista
	for l in list_imagens:
		if l == '':
			#print('AHCLSSLSLSLL')
			list_imagens.remove(l)
	
	
	length = len(list_imagens)
	print ('length 2',length)
	count = randint(0,length-1)
	img = IMG_DIR+list_imagens[count]
	#print(len(img))
	#print(list_imagens)

	url_img = URL_BASE+img
	#print(url_img)
	imagem =[{'img': url_img}]
	return jsonify(imagem=imagem)

