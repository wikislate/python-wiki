#!/usr/local/bin/python3
dict = {'Name': 'Vivek', 'EMP-ID': 694, 'Team': 'DevOps', 'Company': 'hCentive', 'DOJ': '25-08-2014'}

print("Total Items in dictionary:", len(dict))

string = str(dict)
print("String:", string)

dict1 = dict.copy()
print("New copy:", dict1)

tup = ('name', 'class', 'roll-number', 'total-marks')
dict2 = dict.fromkeys(tup)
print("Dictionary form tuple:",dict2)

list1 = ['apple', 'banana', 'pear', 'peach', 'grapes', 'mango']
dict3 = dict.fromkeys(list1,10)
print("Dictionary from list:",dict3)

print("Access using key : %s" %  dict1.get('EMP-ID'))
print("Access value : %s" %  dict1.get('DOB',"Key not found!"))

if 'DOJ' in dict: print("Date of joining: %s" % dict['DOJ'])

print ("Dictionary Items : %s" %  dict.items())

print ("Dictionary Keys : %s" %  dict.keys())

print ("Dictionary Values : ",  dict.values())

print ("List from Values : ",  list(dict.values()))

print ("Tuple from Values : ",  tuple(dict.values()))

dict4 = {'Name': 'Shakun', 'EMP-ID': 917, 'Company': 'Gemalto', 'DOJ': '??-??-2016'}
dict.update(dict4)
print(dict)

print ("Set value if not exists : %s" %  dict.setdefault('Company', None))
print ("Value : %s" %  dict.setdefault('DOB', '17-09-1987'))
print (dict)
