#----------------------------------------------------------------#
# File name: csv_splitter.py
# Author: Youssef Riahi
# Date created: 01/18/2016
# Date last modified: 01/19/2016
# Script version: 2.1
# Python Version: 2.7.10

# Description:
# 	A python script that split a csv into individal csv files
# 		based on the text value of a give column. In this use case
# 		we split files based a site name (community).
# Notes:
# 	update 'delimiter','quotechar' and 'quoting' to match requirements
# 	see import section below for requirements. 'pip install' if needed
# 
# 
# Usage: 
# 	python split_csv_report.py yourcsvfile
#----------------------------------------------------------------#

import csv
from sys import argv
from progressbar import ProgressBar

# assign a short variable name to the progress bar function
pbar = ProgressBar() 

# setting csv file as source file
script, yourcsvfile = argv

# list of portal sites; for now it is a hardcoded list
portal_sites = ['ago', 'anf', 'auditor', 'berkshireda', 'capeda',\
 'childadvocate', 'cjc', 'courts', 'dor', 'dppc', 'edu', 'eea', 'elders',\
  'eohhs', 'eopss', 'essexda', 'essexsheriff', 'ethics', 'governor', 'hdc',\
   'hed', 'ig', 'informedma', 'itdemployee', 'lwd', 'massworkforce', 'mcad',\
    'mdaa', 'mova', 'msa', 'mtrs', 'ocabr', 'osc', 'pca', 'perac', 'portal',\
     'recovery', 'srbtf', 'treasury', 'veterans', 'women']

# loop through portal sites with progressbar
for portal_site in pbar(portal_sites):
	
	# filename formatting
	portal_site_file_name = str(portal_site) + '_analytics_cms.csv'
	portal_site_file = portal_site_file_name

	# create the files
	site_file = open(portal_site_file, 'w')
	
	# specify the column names that will go in the header of each file
	column_names = ['content_id', 'system_title', 'full_title', 'page_desc',\
	 'date_created', 'date_modified', 'content_type', 'ctype_id',\
	  'content_state', 'community', 'content_author', 'url']
	
	# using csv. dictionary writer, we will create the output files
	# we also specify separator and other params
	site_file_writer = csv.DictWriter(site_file, fieldnames=column_names,\
	 delimiter=',', quotechar='=', quoting=csv.QUOTE_ALL)
	
	# after the empty files are created, we add a header to each
	site_file_writer.writeheader()

	# now we are ready to open the input file that we are splitting
	# file is opened in ready binary mode
	csv_file = open(yourcsvfile, 'rb')

	# after the input file is opened, dictionary reader object is created
	# we also specify separator and other params
	my_csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='=')

	# input file rows loop; if match found write it to site_file output file
	for row in my_csv_reader:	
		if row['community'] == portal_site:
			site_file_writer.writerow(row)
	csv_file.close()
