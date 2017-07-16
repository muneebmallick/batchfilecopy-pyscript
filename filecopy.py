import shutil
import os
import datetime

datetime = datetime.datetime.now().strftime("%Y%m%d")
conti='Y'

def exten():
	while True:
		try:
			print 'Please enter Extension types (Comma-Separated):'
			ext = tuple(str(x.strip()) for x in raw_input().split(','))
			if ext.startswith('.'):
				return(ext)
		except ValueError:
			if not ext:
				raise ValueError('Please input extension types')
			else:
				raise ValueError('Not a valid extension type')


def createfolder(datefolder, user_input_dest):
	if datefolder == 'Y':
		destination = user_input_dest +'_'+datetime
		if not os.path.exists(destination):
			os.makedirs(destination)
		
	elif datefolder == 'N':
		if not os.path.exists(user_input_dest):
			os.makedirs(user_input_dest)
		destination = user_input_dest
		
	return destination


def no_walk(src, dest, x):
	try:
		source = os.listdir(src)
		os.chdir(src)

		count = 0
		for files in source:
			if files.endswith(ext):
				if x == "C":
					shutil.copy(files, dest)
					count += 1

				elif x == "M":
					shutil.move(files, dest)
					count += 1

		print '\n', count, ' Files Copied'
		print 'Completed!'

	except WindowsError, e:
		print(e)


def directory_walk(src, dest, x):
	source = os.walk(src)
	os.chdir(src)

	count = 0
	for path, dirs, files in source:
		for file in files:
			if file.endswith(ext):
				path_file = os.path.join(path, file)
				if x == "C":
					shutil.copy2(path_file, dest)
					count += 1
				
				elif x == "M":
					shutil.move(path_file, dest)
					count += 1

				else:
					print "Wrong Input! Please input C or M!"
	
	print '\n', count, ' Files Copied'	
	print 'Completed!'


if __name__ == "__main__":
	
	while conti=='Y':

		user_input_source = raw_input('Please enter Source directory: \n')
		user_input_dest = raw_input('Please enter Destination directory: \n')
		print 'Please enter Extension types (Comma-Separated):'
		ext = tuple(str(x.strip()) for x in raw_input().split(','))
		
		print 'Do you want a new directory created with this name and date? Y or N'
		datefolder = raw_input().upper()
		new_dest = createfolder(datefolder, user_input_dest)

		directory = raw_input("Directory Walk Search? Y or N \n" ).upper()
		
		if directory == "Y":
			x = raw_input("Copy [C] or Move [M]? \n" ).upper()
			directory_walk(user_input_source, new_dest, x)

			conti = raw_input('Continue? Input Y or N \n').upper()

		elif directory == "N":
			x = raw_input("Copy [C] or Move [M]? \n" ).upper()
			no_walk(user_input_source, new_dest, x)

			conti = raw_input('Continue? Input Y or N \n').upper()

		else:
			print "Wrond Input! Please input Y or N!"
#C:\Users\CMMALLI\Desktop\pyth