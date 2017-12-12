"""
*Author: Paulo Jorge
*
*Arquivo responsavel por possuir toda a logica da selecao de anuncios
*
"""
from db import file

"""
*
*funcao para le todo conteudo da base de dados (/base_dados/base) 
*
"""
def motor(file):
	
	linksf = file.read()
	links = linksf.split(';')
	#print(links)
	return links
		
motor(file)