#!/usr/bin/python3

dict = {'Name': 'Vivek', 'EMP-ID': 694, 'Team': 'DevOps', 'DOJ': '25-08-2014', 'DOB': '28-12-1983'};
for key in dict:
	print(key)
key = input("Enter key: ")
try:
	print ("Record found: ", dict[key])
except KeyError as e:
	print("Key not found: ", e)
