"""
*Author: Paulo Jorge


"""


import os


"""

**Esta funcao le os nemes dos arquivos de imagem localizadas 
**no diretorio /static/img

"""
def ready_dir_img():

	#'filename' recebe os nomes e extensao dos arquivos
	filename = os.listdir('static/img')
	#print('flename ',filename)
	return filename

"""

**Esta funcao grava no arquivo '/base_dados/base' os nome e extensao
**dos arquivos imagens do diretorio '/static/img'

"""
def write_database():
	file = open('/../base_dados/base','w')
	#print(file)
	filelist = ready_dir_img()
	#print('filelist ',filelist)

	text = []
	for f in filelist:
		file.write(f)
		file.write(';')
		
	file.close()
	#Lendo a base de dados
	return file
	
def ready_database():
	file = write_database()
	file = open('../base_dados/base','r')
	return file


#print(ready_database())