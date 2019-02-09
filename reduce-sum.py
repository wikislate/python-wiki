# priting summation using reduce() 

# importing functools for reduce() 
import functools

lis = [ 1, 3, 4, 10, 4 ]

print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
