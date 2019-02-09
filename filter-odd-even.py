# a list contains both even and odd numbers.  
seq = [0, 1, 2, 3, 5, 8, 13] 
  
odd = filter(lambda x: x % 2, seq) 
print(list(odd)) 
  
even = filter(lambda x: x % 2 == 0, seq) 
print(list(even))
