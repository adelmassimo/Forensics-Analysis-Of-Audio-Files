import os

if len(sys.argv) > 1:
	root = sys.argv[1]
else:
	print "not enought arguments"

i = 0
for folder in os.listdir(root):
	if os.path.isdir(root + folder) and folder[0:2] != 'F0':
		if i <= 9:
			os.rename(root + folder, root + 'D000' + str(i) + '_' + folder)		#cambia nome alle cartelle
		else:
			os.rename(root + folder, root + 'D00' + str(i) + '_' + folder)		#cambia nome alle cartelle
		i = i+1

i = 0
for folder in os.listdir(root):
	folderpath = root + folder + '/' 
	if os.path.isdir(folderpath):
		for file in os.listdir(folderpath):			#cambia nome ai file dentro le cartelle
			if os.path.isfile(folderpath + file) and file != '.DS_Store':
				splittedFile = file.split('.')
				suffix = splittedFile[len(splittedFile)-1]
				if i <= 9:
					os.rename(folderpath + file, folderpath + folder[6:] + '_sample' + str(i) + '.' + suffix)
				else:
					os.rename(folderpath + file, folderpath + folder[6:] + '_sample' + str(i) + '.' + suffix)
				i = i+1

		i = 0
