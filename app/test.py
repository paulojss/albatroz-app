from db import file
from motor import motor

motor = motor(file=file)
def agora():
	titulo,img = motor.split(',')
	print(titulo+' '+img)

agora()