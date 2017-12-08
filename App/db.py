import os


file = open('../base_dados/base','r')

def readyDirImg():
	filename = os.listdir('../static/img')
	return filename

def writeDataBase():
	file = open('../base_dados/base','w')
	filelist = readyDirImg()
	
	text = []
	for f in filelist:
		text = f
		file.write(f)
		file.write(';')
		
	file.close()

writeDataBase()

