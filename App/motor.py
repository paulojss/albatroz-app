"""
*
*Arquivo responsavel por possuir toda a logica da selecao de anuncios
*
"""
from db import file

"""
*
*funcao para trabalhar a base dados 
*
"""
def motor(file):

	linksf = file.read()
	links = linksf.split(';')
	#print(links)
	return links
		
motor(file)