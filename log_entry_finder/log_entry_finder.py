import os
import sys
from sys import argv
import re
import csv

# setting up the script params
script, logs_path, my_string = argv

# pattern to search for
my_pattern = my_string

# print string to look to screen
print '[ ===> ] Searching for:  %s' % (my_pattern)

# list to hold logfiles for the processing loop
log_files_list = []

# list of matching lines
matching_lines = []

# find the log files in the logs folder
def get_log_files():
	for root, dirs, files in os.walk(str(logs_path)):
		for f in files:
			log_files_list.append(os.path.join(root, f))

# execute function to get list of files
get_log_files()

# log files loop for processing
for one_log in log_files_list:
	# show some progress to screen
	print '[ + ] Searching file %s' % (one_log)

	# open log file in read mode
	fp = open(one_log, 'r')

	# loop through log files
	for line in fp:
		if re.search(my_pattern, line):
			matching_lines.append(line)
			# print line

# create results file in write / append mode
result_file = open("output_matches.csv",'wa')

# feed the files to csv file handler
my_writer = csv.writer(result_file)

# write the matching lines to a file
print '[ ===> ] Writing matches to file...'
for line in matching_lines:
	my_writer.writerow([line])
