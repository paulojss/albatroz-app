from flask import Flask, render_template
from urllib import request
import json


app = Flask(__name__)

@app.route('/')
def index():
	response = request.urlopen('http://127.0.0.1:5000/ns/v1')
	
	dicionario = json.loads(response.read().decode('ISO-8859-1'))
	url = dicionario['url']
	print(url)
	return render_template('index.html',url=url)


if __name__ == '__main__':
	app.run(port=8000, debug=True)