# Add two lists using map and lambda 
  
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 

# Add three lists using map and lambda 
  
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
numbers3 = [7, 8, 9]
  
result = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3) 
print(list(result)) 
