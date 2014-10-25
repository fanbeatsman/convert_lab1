import sys
import os
from subprocess import Popen


list_of_files={}
currentdir = os.getcwd()
for(dirpath,dirnames,filenames) in os.walk(currentdir):
	for filename in filenames:
		if filename[-4:] == '.zvi':
			
			list_of_files[filename]=os.sep.join([dirpath, filename])
						

for a_file in list_of_files:
	extension_correction = a_file
	extension_correction=extension_correction[:-4]
	extension_correction=extension_correction+".tif"
	command="bfconvert.bat " + list_of_files[a_file] + " " + extension_correction
	p=Popen(command)
	#os.system(command)

	
print (list_of_files)
