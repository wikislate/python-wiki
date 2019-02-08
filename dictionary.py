#!/usr/local/bin/python3
dict = {'Name': 'Vivek', 'EMP-ID': 694, 'Team': 'DevOps'}
print("Dictionary:", dict)

print("dict['Name']:", dict['Name'])
print("dict['Team']:", dict['Team'])

print("All keys:")
for key in dict: print(key)

print("All values:")
for a,b in dict.items(): print(b)

print("All key:value pairs")
for key,value in dict.items(): print(key, ":", value)

print("Adding New key:value")
dict['Company'] = 'hCentive'
dict['DOJ'] = 'NA'
print(dict)

print("Updating existing value")
dict['DOJ'] = '25-08-2014'
print(dict)

print("Remove a dictionary entry")
del dict['Company']
print(dict)

print("Clear all dictionary entries")
dict.clear()
print(dict)

print("Delete dictionary")
del dict
print(dict)
