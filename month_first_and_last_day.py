#----------------------------------------------------------------#
# File name: month_first_and_last_day.py
# Author: Youssef Riahi
# Date created: 03/31/2016
#----------------------------------------------------------------#
# description: 
# the script gets the first and last day of month based input year.
# output is a dictionary of months with fist and and last day.
# data (order of months) is not sorted yet.
#   
# usage example:
# python month_first_and_last_day.py 2015
#----------------------------------------------------------------#
from sys import argv
import calendar

script, input_year = argv

def get_ranges(input_year):
	# empty dictionary to store month name, first and last day
	input_year_ranges = {}

	# 12 months loop
	for i in range (0,12):
		# fix the starting month to 1
		m = i+1
		
		# clean month digit by adding a leading zero
		cleaned_month_digit = str(m)
		if len(cleaned_month_digit) == 1:
			cleaned_month_digit = str(0) + cleaned_month_digit

		# create an empty list to store days of current month
		month_days_list = []
		
		# create a calendar object
		cal = calendar.Calendar()
		
		# get all days in month and add to list
		for i in cal.itermonthdays(int(input_year), m):
			if i == 0:
				pass
			else:
				# add day numbers to current month list
				month_days_list.append(i)
		
		# month name in current locale
		locale_month_name = calendar.month_name[m]

		# clean day digit by adding a leading zero
		fd = month_days_list[0]
		if len(str(fd)) == 1:
			fd = str(0) + str(fd)
			# last day of month
		ld = month_days_list[-1]
		
		# first and last day format
		# example: 2015-02-28
		first_day = str(input_year) + '-' + str(cleaned_month_digit) + '-' + str(fd)
		last_day = str(input_year) + '-' + str(cleaned_month_digit) + '-' + str(ld)
		
		# dictionary for start and end day of month
		month_property = {'start': first_day, 'end': last_day}

		# set month as dictionary
		input_year_ranges[locale_month_name] = {}
		
		# add 'start' key to month dictionary
		input_year_ranges[locale_month_name]['start'] = first_day
		
		# add 'end' key to month dictionary
		input_year_ranges[locale_month_name]['end'] = last_day

	return input_year_ranges

# print a dictionary of months with their first and last day according to year
for month, first_and_last_day in get_ranges(input_year).iteritems():
	print month, first_and_last_day
