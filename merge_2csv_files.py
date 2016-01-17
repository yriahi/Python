#----------------------------------------------------------------#
# File name: merge_csv_files.py
# Author: Youssef Riahi
# Date created: 01/13/2016
# Date last modified: 01/17/2016
# Script version: 1.0
# Python Version: 2.7.10

# Usage: 'python merge_csv_files.py cms.csv ga.tsv'
# Added dtype='unicode' to avoid the error: "have mixed types. Specify dtype option on import or set low_memory=False."
# Script can detect column names; useful to fine target key(s) to be merged on
# Option for 'inner merge' available; but currently commented out.
# The script merges a csv with a tsv. 
# sep=',', quotechar='=' can be changed to match other sep/quotechar
#----------------------------------------------------------------#
 
from sys import argv
import pandas
pandas.set_option('display.expand_frame_repr', False)

# Feeding the 2 files to the scripts
script, yourfile1, yourfile2 = argv


# first file is content from cms in csv format
# add verbose=True for metrics 
file_1_df = pandas.read_csv(yourfile1, dtype='unicode', sep=',', quotechar='=', keep_default_na=False, na_values=[""])

# second file is Google Analytics in tab separated values format.
file_2_df = pandas.read_csv(yourfile2, dtype='unicode', sep='\t', keep_default_na=False, na_values=[""])

# use '.columns' to view and identify appropriate join keys
# print file_1_df.columns
# print file_2_df.columns

# read and/or test with first 10 lines 
# this is useful for quick sampling/testing purposes
# file_1 = file_1_df.head(10)
# file_2 = file_2_df.head(10)

# content from file 1
file_1 = file_1_df

# content from file 2
file_2 = file_2_df

# depending on the the type of merge, uncomment the appropriate line and change column as needed.
# merged_inner = pandas.merge(left=file_1,right=file_2, left_on='url', right_on='url')
merged_left = pandas.merge(left=file_1,right=file_2, how='left', left_on='url', right_on='ga:pagePath')

# write merged data to file system
merged_left.to_csv('cms_ga.csv')

# print merged data to screen; comment/uncomment as needed
print merged_left


