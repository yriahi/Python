#----------------------------------------------------------------#
# File name: Find_All_File_Extensions_in_Target_Folder.py
# Author: Youssef Riahi
# Date created: 11/10/2015
# Date last modified: 12/14/2015
# Script version: 1.0
# Python Version: 2.7.10
#----------------------------------------------------------------
# 1.0 - Initial version to get extensions by folder
#----------------------------------------------------------------#
'''
Description: 
	A python script that:
		- Count all files scanned in the target folder (recursive)
		- Count unique file extensions
		- Find files that have no extension
		- Print a count for each extension
Notes: 
	- The script accepts 1 argument: the target folder
Usage: 
	python Find_All_File_Extensions_in_Target_Folder.py /yourpath/
'''

import sys, os
from sys import argv
from os import walk, path
from collections import Counter
from prettytable import PrettyTable

# this python script only has one argument so far :-)
script, yourpath = argv

# create an empty list for files with or without extensions.
Files_Scanned = []
Extensions = []
NoExtensions = []
NoExtensions_List = []

# get all extensions or no extensions in the target directory
def GetTargetFolderExtensions():
   # recursive walk of folders
   for root, dirs, files in os.walk(str(yourpath)):
      for f in files:
        # check for files that have no extension
        if os.path.splitext(f)[1][1:] == '':
        	# keep track of files with 'no extension'
        	NoExtensions.append(os.path.splitext(f)[1][1:])
        	# track all files with no extension
        	NoExtensions_List.append(os.path.join(root, f))
        else:
        	# keep track of files that have an extension
        	Extensions.append(os.path.splitext(f)[1][1:])
        	# track all files with extension
        	Files_Scanned.append(os.path.join(root, f))

GetTargetFolderExtensions()

Summary = PrettyTable(['Total files', 'Extensions found', 'No extensions'])
Summary.align['Total files'] = 'l' # Left align city names
Summary.padding_width = 1 # One space between column edges and contents (default)
Summary.add_row([len(Files_Scanned), len(Counter(Extensions)), len(NoExtensions)])
print Summary

# print list of files with no extension
#for NoExtension_File in NoExtensions_List:
#	print NoExtension_File

# print list of files with that have an extension
#for File_Scanned in Files_Scanned:
#	print File_Scanned

# Extensions is a list if files extensions with duplicates
# we want to get a count for each files extension: convert to Counter object
Extensions_List_Details = Counter(Extensions)
# this shows the extensions and a count for each type
for key, value in Extensions_List_Details.iteritems():
	print key, value


