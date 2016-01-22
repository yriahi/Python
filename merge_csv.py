#----------------------------------------------------------------#
# File name: merge_2csv_files.py
# Author: Youssef Riahi
# Date created: 01/13/2016
# Date last modified: 01/17/2016
# Script version: 1.1
# Python Version: 2.7.10
# 
# Description: 
# 	A python script that merges 2 csv files on a certain column.
# 	This use case does a merge on the 'url' column between a content management system report
# 	and a Google Analytics report. The latter is in tsv format. 
# 
# Usage: 
#	'python merge_csv_files.py yourfile1.csv yourfile2.tsv'
# 
# Notes:
# 	Added dtype='unicode' to avoid the error: "have mixed types. Specify dtype option on import or set low_memory=False."
# 	Script can detect column names; useful to find target key(s) to be merged on.
# 	Option for 'inner merge' available; but currently commented out.
# 	Script can merge other csv formats as long as 'sep' and 'quotechar' are updated accordingly.
#----------------------------------------------------------------#
 
from sys import argv
import pandas

# From Pandas Docs: Whether to print out the full DataFrame repr for wide DataFrames across multiple lines.
# This is for screen printing only; and does not affect merged csv output.
pandas.set_option('display.expand_frame_repr', False)

# Feeding the 2 files to the script.
# Usage again is : python merge_2csv_files.py cms.csv ga.tsv
script, yourfile1, yourfile2 = argv


# 'dtype' Data type objects: How the bytes should be interpreted.
# 'sep' Delimiter to use. If sep is None, will try to automatically determine this. Regular expressions are accepted.
# 'quotechar' The character used to denote the start and end of a quoted item.
# 'keep_default_na' : If na_values are specified and keep_default_na is False the default NaN values are overridden, otherwise they are appended to.
# na_values : Additional strings to recognize as NA/NaN
# change to 'verbose=True' if you want to see metrics on screen.
#
# file 1 is a cms report that is being merged a with Google Analytics report 
file_1_df = pandas.read_csv(yourfile1, dtype='unicode', sep=',', quotechar='=', keep_default_na=False, na_values=[""], verbose=True)

# file 2 is Google Analytics report in tsv format being merged with a cms report (file 1 above).
file_2_df = pandas.read_csv(yourfile2, dtype='unicode', sep='\t', keep_default_na=False, na_values=[""], verbose=True)

# use '.columns' to print colmun names to screen. It is handy to identify appropriate join keys.
# print file_1_df.columns
# print file_2_df.columns

# this is useful for quick sampling/testing purposes
# read and/or test with first 10 lines 
# file_1 = file_1_df.head(10)
# file_2 = file_2_df.head(10)

# content from file 1
file_1 = file_1_df

# content from file 2
file_2 = file_2_df

# depending on the the type of merge being done, uncomment the appropriate line.
# 
# '.merge' merges objects by performing a database-style join operation by columns or indexes.
# Available options are: left, right, outer, inner. The default is 'inner'
# More details here: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html

# Option 1: inner
# inner: use intersection of keys from both frames (SQL: inner join)
# 'how' is not specified here because it is the default behaviour or merge in pandas.
# merged_inner = pandas.merge(left=file_1, right=file_2, left_on='url', right_on='url')

# Option 2: left
# left: use only keys from left frame (SQL: left outer join)
merged_left = pandas.merge(left=file_1, right=file_2, left_on='url', right_on='ga:pagePath', how='left')

# write merged data to file system
merged_left.to_csv('cms_ga.csv')

# print merged data to screen; comment/uncomment as needed
print merged_left


