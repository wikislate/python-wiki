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
		print("Message")
		a++
	while a < 10:
		if a == 5:
			continue
		print(a)
		a++
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
		c = a + beniwal
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
		a = nested(a)
		return a
	
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
	
	f = lambda c: lambda a, b:lambda d: (c * (a + b)) %d
	print(f(2)(4,3)(11))
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
		raise

## Practice files
1. helloworld.py
2. conditional.py
3. if_else_oneline.py
4. while_fibonacci.py
5. for_readfile.py
