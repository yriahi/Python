#----------------------------------------------------------------#
# File name: siteimprove_summary.py
# Author: Youssef Riahi
# Date created: 01/20/2016
# Date last modified: 01/22/2016
# Script version: 1.1
# Python Version: 2.7.10

# Description:
# 	Connect to a siteimprove account and get a summary
# 	of site names with the total of broken links (by site)
# 
# Notes:
# 	requires api access; update api_user and api_key accordingly
# 
# Usage: 
# 	python siteimprove.py
# 
# Updates:
#	added 'prettytable' for formatting
#----------------------------------------------------------------#

import requests                       # http://docs.python-requests.org/en/latest/
import json                           # https://docs.python.org/2/library/json.html
from prettytable import PrettyTable   # https://code.google.com/p/prettytable/

# api user and key
api_user = "***EMAIL***";
api_key = "***API_KEY***";

# api url being accessed
# '/sites' is a summary/overview for all sites
resource = "https://api.siteimprove.com/v1/sites"

# connect to api and feed returned data to json
response = requests.get(resource, auth=(api_user, api_key))
account = response.json()

# this work only for the top root api url:
# https://api.siteimprove.com/v1
# print account.get("account_name")

# show total number of sites available on account
# api returns paginated data
# total of all sites is available in 'page 1'
print 'Total sites: ' + str(account['total_items'])

# get total pages in pagination
# api returns pagination total in page 1
pagination_total = account['total_pages']
# print 'Pagination total = %s' % (pagination_total)

def get_siteimprove_account_summary():
	# setting up table header: 'site_name' and 'broken_links' columns
	qa_account_summary = PrettyTable(["Site Name", "Broken Link Count"])

	# One space between column edges and contents (default)
	qa_account_summary.padding_width = 1
	
	# Left align 'site_name'
	qa_account_summary.align["Site Name"] = "l" 

	# loop for pagiantion range
	for pagination_item in range(pagination_total):
		
		# since items in list start with '0', no good if added to base url. so...
		# we increment by '1'; then we go from there
		pagination_url =  'https://api.siteimprove.com/v1/sites?page=%d' % (int(pagination_item) + 1)
		
		# connect to each page in pagination and get a response
		pagination_response = requests.get(pagination_url, auth=(api_user, api_key))
		my_account = pagination_response.json()
		
		# print pagination_response.status_code
		websites = my_account['items']
		for website in websites:
			# print website['site_name'], website['broken_link_count']
			qa_account_summary.add_row([website['site_name'], website['broken_link_count']])
			# loop key:value for each site
			# for key, value in website.iteritems():
			# 	print key, value
		print qa_account_summary

summary = get_siteimprove_account_summary()

