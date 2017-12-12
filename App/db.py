"""
*Author: Paulo Jorge


"""


import os


file = open('../base_dados/base','r')

"""

**Esta funcao le os nemes dos arquivos de imagem localizadas 
**no diretorio /static/img

"""
def readyDirImg():

	#'filename' recebe os nomes e extensao dos arquivos
	filename = os.listdir('static/img')
	#print('flename ',filename)
	return filename

"""

**Esta funcao grava no arquivo '/base_dados/base' os nome e extensao
**dos arquivos imagens do diretorio '/static/img'

"""
def writeDataBase():
	file = open('../base_dados/base5','w')
	#print(file)
	filelist = readyDirImg()
	#print(filelist)

	text = []
	for f in filelist:
		text = f
		file.write(f)
		file.write(';')
		
	file.close()

writeDataBase()

