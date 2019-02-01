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
## Practice files
1. helloworld.py
2. conditional.py
3. if_else_oneline.py
4. while_fibonacci.py
5. for_readfile.py
