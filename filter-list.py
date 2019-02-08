# function that filters fruits in demand from available in stock 
def fun(fruit): 
    demand = ['guava', 'grapes', 'berries', 'sapota', 'banana'] 
    if (fruit in demand): 
        return True
    else: 
        return False
  
stock = ['guava', 'grapes', 'apple', 'strawberry', 'sapota', 'banana'] 
  
filtered = filter(fun, stock) 
  
print(' Fruits in stock are:') 
for s in filtered: 
    print(s) 
