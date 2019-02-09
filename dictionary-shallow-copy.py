#!/usr/local/bin/python3

dct = { 'Item': 'Shirt', 'Size': 'Medium', 'Color': 'Pink' }
dct1 = dct
dct2 = dct.copy()
print("Main Dictionary:",dct)
print("Copy of main dictionary:", dct1)
print("Shallow copy of main dictionary:", dct2)

print("---------- Updating main dictionary ----------")
dct['Size'] = 'Small'
print("Copy of main dictionary:", dct1)
print("Shallow copy of main dictionary:", dct2)
