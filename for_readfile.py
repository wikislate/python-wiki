#!/usr/local/bin/python3

#Read lines from the file
fh = open('README.md')
for line in fh.readlines():
	print(line, end='') #end null removes default new line character by print
