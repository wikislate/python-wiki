# python-wiki
## Tutorial
1. Datatype
	>>> type(3)
	<class 'int'>
	>>> type(3.5)
	<class 'float'>
	>>> type('s')
	<class 'str'>
	>>> type('asd')
	<class 'str'>
	>>> type(True)
	<class 'bool'>
	>>> type(False)
	<class 'bool'>

2. Variable
Assign value
	varN = 34
	varF = 3.6
	varS = "vivek"
	a = b = c = 4.5
	varN, varF, varS = 3, 3.5, 'vivek'
	varN = varS # Automatically takes care of typecasting
Print
	print(varF)
	print(varS)
	
3. comments
Single-line, inline 
	# Comment
Multi-line
	... 
	comment
	comment
	...

4. Expressions
Basic Arithmetic
- Basic Operators (+ - * / %)
- Exponent Operator(**)
Auto typecasting
	print(2+5) # Yields integer type 
	print(3.5+5) # Yields floating point type
Division Characteristics
- Force to floating point
	print(32.0/5)
- Force to rounded down (nothing or 0 after floating point)
	print(32//5) # 6
	print(32.0//5) # 6.0
Assign to variables
	a = 5 + 6
	b = 3.6 * 9
	c = 34 % 5
Operator Precedence
	() ** * / & + -
Binary Number Manipulation
	print(1 << 3) # Left shift 1 shifts to 3 place left resulting 8
	print(32 >> 4) # Right shift 32 (100000) shifts to 5 place right resulting 1
	print(256 & 255) # 1000000000 AND 0111111111, applies AND with each bit place resulting 0000000000
	print(256 | 255) # 1000000000 OR 0111111111, applies OR with each bit place resulting 1111111111 ie 511
	print(60 ^ 13) # 00111100 XOR 00001101, resulting 00110001 ie 49

4. Strings
Basic string manipulation
	string='This is a string in python.' # or ""
	string[0]
	len('It calculates the length of this string')
	len(string) # Using variables
	print(string[-1]) # inverse indexing, returns last character of string, -2 for 2nd to last.
	string[5:11] # Returns part of the string start from 5 to next 11 characters
	string[:5] # Everything upto 5
	string[5:] # Everything from 5 all the way upto the end.
Concatenation 
	string = 'Con' + 'catenation' # + operator is optional
	string = 2 * ('Vivek' + 'Beniwal') # Print concatenated string twice
	a = 'vivek'
	b = 'beniwal'
	print(a + b)	# + operator is mandatory while using variables
Replace Character
	word = "Ford" 
	word = 'L' +word[1:]
Format Methods
	print("Today I had {0} cups of {1}".format(3,"coffee")) # Indexing or Index number or positional arguments
	print("Dimensions: ({x}, {y}, {z})".format(x = 4.0, y = 3.2, z = 4.1)) # Using variables
	print("{model} has {0}G RAM and {1}G storage.".format(6,64, model = 'Galaxy S9 Plus'))
	print('{:<20}'.format("text")) # Left alignment 20 spaces
	print('{:>20}'.format("text")) # Right alignment 20 spaces
	print('{:b}'.format(43)) # Binary output
	print('{:x}'.format(43)) # Hexadecimal
	print('{:o}'.format(43)) # Octal
Format Output
	print("""\
				Hello,
						This is my message.
				This is another line.
				Thanks & Regards
				Vivek Beniwal
				""")
5. Branching
Logical Operators (< > <= >= != ==), (not and or)
	print(3 < 9) # Conditional operator returns boolean value
	print(not var)
	print(var and var1)
if statement
	drink = 'milk'
	if drink == milk or drink == buttermilk:
		print("Not lactose intolerant")
if else statement
	drink = 'milk'
	if drink == milk or drink == buttermilk:
		print("Not lactose intolerant")		
	else:
		print("Lactose intolerant")
if elif statement
	if drink == milk:
		print("Milk")
	elif drink == buttermilk:
		print("Buttermilk")		
	else:
		print("Lactose intolerant")
Ternary operator
	print("a is small" if a < b else "a is not small")
	a = 7 if 3**3 > b else 14
	print(a)
6. Loops
For loop
	range(start,end,step) # range(0,4,2) step is increment, here 2, default 1, range is start to end-1
	for i in range(1,10):
		print(i)
		
	for i in range(len(string)):
		print(string[i])
	
	for i in string:
		print(i)
While loop
	while condition != 0:
		print(condition)
		condition = condition - 1
Break and continue statement
	while a < 10:
		if a == 5:
			break
		print(a)
		a+=1
	while a < 10:
		a+=1
		if a == 5:
			continue
		print(a)
		
7. Functions
Basic definition
	def function():
		print("This is our first function")
	
	function()	# Function call

Function with return
	def returning():
		return "This is our first function"
	
	print(returning())	# Function call
	...
	result = resulting()
	print(result)
	...

Multiple value return	
	def multival():
		return "This is a result",2
	print(multival())
	
Passing parameters
	def parameters(a):
		print(a)

	parameters("This is a parameter")
	
	def add(a,b):
		c = a + b
		return c
		
	result = add(43,66)
	print(result)

Default parameters
	def default_param(a, b = 6, c = 8):
		return a + b + c
	
	result = default_param(7) # 7 is value of a
	print(result)
	
Scope
	def scope(a):
		a = a + 1
		print(a)
		return a
	scope(6)
	print(a) # error not defined

	def outer(a):
		def nested(b):
			return b * a; # use ; when nested
		x = nested(a)
		return x
	
	print(outer(4))
	
	def f(a):
		def g(b):
			return a * b
		return g
	print(f(6)(4))
	
	def f(a):
		def g(b):
			def h(c):
				return a * b * c
			return h
		return g
	print(f(6)(4)(3))

Recursive function
	def factorial(n):
		if n == 1:
			return 1
		else:
			return n * factorial(n-1)
	
	print(factorial(5))
	
Regular recursion 
	def sum(n):
			if n == 1:
				return 1
			else:
				return n + sum(n-1)

Tail recursion
	def tail_sum(n, accumulator = 0):
		if n == 0:
			return accumulator
		else:
			return tail_sum(n-1,accumulator+n)
	
	print(sum(10))
	print(tail_sum(10))
Lambda Function
	f = lambda x, y: x + y
	print(f(2,5))
	
	f = lambda a: lambda b: lambda c: a * b * c
	print(f(7)(8)(9))
	
	f = lambda c: lambda a, b:lambda d: (c * (a + b)) % d
	print(f(2)(4,3)(11))
	
	def adder(x):
		return lambda y: x + y
	add9 = adder(9)
	add9(7)
	
8. Exception Handling
Exceptions and Errors
	print(4/0)
	file = open("file","r") # Opening a non-existing file
	int('1.2') # Value Error
Handling Exceptions
	try:
		a = 5/0
	except Exception as e:
		print(e)
		
	try:
		n = int(input("Enter an Integer: "))
	except ValueError:
		print("That is not an integer")
		
	try:
		sum = 0
		file = open('numbers.txt','r')
		for number in file:
			sum = sum + 1.0/int(number)
		print(sum)
	except ZeroDivisionError:
		print("Number in file equal to zero!")
	except IOError:
		print("File DNE")
	finally:
		print(sum)
		file.close()
Throwing Exceptions
	a = 1
	def RaiseException(a):
		if type(a) != type('a'):
			raise ValueError("This is not string")
	try:
		RaiseException(a)
	except ValueError as e:
		print(e)
		
	def TestCase(a , b):
		assert a < b, "a is greater than b"
	try:
		TestCase(2,1)
	except AssertionError as e:
		print(e)
9. Data Input
Data Input setup
	number = input("How many Fibonacci number: ")
	print(number)
File Management
	file = open("/home/wiki/file.txt", "r") # open(filename, access, buffering)
	print(file.read())
	file.close() # After using file close the file
Read a specific number of characters from a file	
	print(file.read(5)) # First five character
	print(file.tell()) # It tells the current position of the pointer in the file.
	file.seek(n) # Move pointer to nth character
Read file per line
	file = open("<path>", "r")
	for line in file
		print(line)
	file.close()
File attributes
	file = open("<path>", "r")
	print("File Name: " + file.name)
	print("is closed: " + str(file.closed))
	print("Mode " + file.mode)
Write to a file
	file = open("file.txt", "w+") # w - write mode, w+ read-write
	file.write("This is new line in the file")
	file.seek(0) # Seek a position to write
	file.write("New text")
	print(file.read())
	file.close()
10. Data Structures
Tuple- Sequence of immutable elements
	tup = ('one', 'two', 'three', 'four', 'five', 'six')
	tup1 = 5, 'pqr', True, False
	tup2 = 'A'
	tup3 = ('A',)		# When there is one element, comma in the end is mandatory 
	print(tup[0])		# Accessing first element
	print(tup[-1])		# Accessing last element
	print(tup[0:2])		# tup[A:B] after Ath upto Bth, here ('one', 'two')
	print(tup[2:5])		# Starting after 2nd upto 5th, here ('three', 'four', 'five')
	try:				# Tuple elements cannot be change
		tup[3] = 5
	axcept Exception as e:
		print(e)
	tup = tup + ('seven',)			# Elements can be added at the end
	tup = tup + ('eight', 'nine')	# Adding multiple elements
	tup = tup + tup1				# Adding two tuple
	print(tup * 5)			# Prints all elements 5 times
	print('six' in tup)		# Boolean output, here True
	for i in tup: print(i)	# traverse a tuple using for loop
	def multiple_result():	# Use in a function to return multiple values
		return(1,2,'abc')
	print(multiple_result())
Built-in Tuple functions
	len(tup)		# Length
	max(tup)		# Maximum value, for string alphabetical order 
	min(tup)		# Minimum value
	tuple(list)		# Convert a list into a tuple 
Lists
	list = ['one', 'two', 'three', 'four', 'five', 'six']
	list1 = [5, 'pqr', True, False, (1, 2)]	# A list containing a tuple
	print(list1[2])				# Accessing an element
	print(list1[-1])			# Accessing the last element
	print(list1[4])				# Accessing tuple from the list
	print(list1[4][0])			# Accessing a tuple element from the list
	print(list1 + ['5'])		# Add an element
	print(list1 * 2)			# Repetition 
	print(2 in list1)			# If element exists or not in the list
	print(list1 == [1, 2, 3])	# Compare lists
	print(list1[:2])			# First 2 elements from the list
	list1[1] = xyz				# Updating a list element
	del list1[2]				# Deleting a list element
	len([1,2,3])				# Length
	list1 + list2				# Concatenation
	for i in list1: print(i)	# Traverse 
Built-in list functions
	len(list)					# Length
	max(list)					# Maximum value
	min(list)					# Minimum value
	list(tup)					# Convert a tuple in to a list
Built-in methods
	list.append(obj)			# Append an object obj in the list
	list.count(obj)				# Count of an object obj
	list.extend(seq)			# Extend a list or tuple in the list
	list.index(obj)				# Returns the lowest index of obj
	list.insert(index, obj)		# Inserts object obj into list at offset index, shifting right all values next to offset index
	list.pop(n)					# Removes object at offset index n, last, if n is not provided
	list.remove(obj)			# Removes object obj from the list
	list.reverse()				# Reverses objects of the list in place
	list.sort()					# Sort the list, not supported if elements are mixed datatype
	
	def addition(n): 
		return n + n 
	# We double all elements of a list/tuple using map() 
	numbers = [1, 2, 3, 4] 
	result = map(addition, numbers) 
	print(list(result)) 
	
	numbers = [1, 2, 3, 4]
	print(list(map(lambda x: x + x, numbers)))		# Using lambda function
	
	print(list(map(lambda x: x + x, [1, 2, 3, 4])))	# Previously undefined list
	
	
## Practice files
1. helloworld.py
2. conditional.py
3. if_else_oneline.py
4. while_fibonacci.py
5. for_readfile.py
6. map.py
7. map-lambda.py
8. map-add-lists.py
9. map-listify.py
10. filter.py
11. filter-list.py
12. filter-odd-even.py
13. reduce-sum.py