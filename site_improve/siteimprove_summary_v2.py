#----------------------------------------------------------------#
# File name: siteimprove_summary_v2.py
# Author: Youssef Riahi
# Date created: 01/20/2016
# Date last modified: 01/24/2016
# Script version: 1.4
# Python Version: 2.7.10
#
# Description:
# 	Connect to a siteimprove account and get a summary
# 	of site names with the total of broken links (by site).
# 	v2 saved paginated data to csv file, read from it then print to screen.
# 
# Notes:
# 	requires api access; update api_user and api_key accordingly
# 
# Usage: 
# 	python siteimprove_summary_v2.py
# 
# Updates:
#	added 'prettytable' for formatting
# 	paginated data is now saved incrementally before final print
# 	paginated data saved to 'all_sites' dict; then printed to screeen
#----------------------------------------------------------------#

import requests                       # http://docs.python-requests.org/en/latest/
import json                           # https://docs.python.org/2/library/json.html
from progressbar import ProgressBar   # https://pypi.python.org/pypi/progressbar
from prettytable import PrettyTable   # https://code.google.com/p/prettytable/
import csv                            # https://docs.python.org/2/library/csv.html

# assign a short name to 'ProgressBar()'
pbar = ProgressBar() 

# siteimprove api: user and key
api_user = "***EMAIL***";
api_key = "***API_KEY***";

# api url being accessed
# '/sites' is a summary/overview for all sites
resource = "https://api.siteimprove.com/v1/sites"

# connect to api and feed returned data to json
response = requests.get(resource, auth=(api_user, api_key))
account = response.json()

# get total pages in pagination
# api returns pagination total in page 1
pagination_total = account['total_pages']
# print 'Pagination total = %s' % (pagination_total)

def get_siteimprove_mysites_summary():
	
	# creating a csv file in mode: 'wa'
	tmp_csv = open('tmp_csv_file.csv', 'wa')

	# setting up the csv writer params
	tmp_csv_writer = csv.writer(tmp_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_ALL)

	# setting up table header: 'site_name' and 'broken_links' columns
	qa_account_summary = PrettyTable(["Site Name", "Broken link count"])

	# one space between column edges and contents (default)
	qa_account_summary.padding_width = 1
	
	# left align 'site_name'
	qa_account_summary.align["Site Name"] = "l" 

	# create empty dict to hold data from pagination
	all_sites = {}

	# loop for pagination range
	for pagination_item in pbar(range(pagination_total)):
		
		# since items in list start with '0', no good if added to 'resource'. so...
		# we increment by '1'; then we go from there
		pagination_url =  'https://api.siteimprove.com/v1/sites?page=%d' % (int(pagination_item) + 1)
		
		# connect to each page in pagination and get a response
		pagination_response = requests.get(pagination_url, auth=(api_user, api_key))
		
		# feed page response to 'json'
		my_account = pagination_response.json()
		
		# loop and add sites from paginated data to csv
		websites = my_account['items']
		for website in websites:
			# adding each site and broken links count to csv
			tmp_csv_writer.writerow([website['site_name'], website['broken_link_count']])
	
	# done writing to csv file
	tmp_csv.close()
	

def render_table_from_csv():
	read_2_table = open('tmp_csv_file.csv', 'r')
	table_reader = csv.reader(read_2_table, delimiter=',', quotechar='|')

	# setting up table header: 'site_name' and 'broken_links' columns
	qa_account_summary = PrettyTable(["Site Name", "Broken Link Count"])

	# One space between column edges and contents (default)
	qa_account_summary.padding_width = 1

	# Left align 'site_name'
	qa_account_summary.align["Site Name"] = "l" 

	for row in table_reader:
		qa_account_summary.add_row([row[0], row[1]])

	print qa_account_summary
	read_2_table.close()


get_siteimprove_mysites_summary()
render_table_from_csv()

# show total number of sites available on account
# api returns paginated data
# total of all sites is available in 'page 1'
print 'Total sites: ' + str(account['total_items'])
