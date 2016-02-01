#----------------------------------------------------------------#
# File name: find_files_by_extension.py
# Author: Youssef Riahi
# Date created:  11/23/2015
# Date last modified:  11/23/2015
# Script version: 1.2
# Python Version: 2.7.10
# 
# Description: 
# 	- A python script that find files by extension in a target folder
#   - See usage format.
#
# Notes: 
# 	- The script accepts 2 arguments: 1- the target folder. 2- File extension. 
# 	- Result may not be accurate if you have files such as FILE_NAME.pdf.bak
# 	- The script relies on "split" to get the file extension.
# 
# Usage: 
# 	python FindFilesByExtension.py /home/user/ pdf
#----------------------------------------------------------------#

import os, sys
from os import path
from sys import argv
from collections import Counter

# stting up script arguments
script, yourpath, yourextension = argv

# save list of file that march your extension
FilesFound = []

# find all files in target directory
# split extension and compare to your extension
# if extension match add to 'FilesFound' list
def FindFilesByExtension():
	for root, dirs, files in os.walk(str(yourpath)):
		for f in files:
			if yourextension == os.path.splitext(f)[1][1:]:
				FilesFound.append(os.path.join(root,f))

def FindFilesByExtensionOut():	
	FindFilesByExtension()
	if len(FilesFound) > 0:
		# print found files to screen
		print FilesFound
		print "Found " + str(len(FilesFound)) + " " + str(yourextension) + " files."
	
	# if no extensions found, display message
	elif len(FilesFound) == 0:
		print "\nFound 0 files with '%s' extension.\n" % (yourextension)
			
FindFilesByExtensionOut()
