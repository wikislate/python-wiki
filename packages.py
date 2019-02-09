# Packages and modules
import main.NumberWordList as pkg
import main.fibonacciFactorial as fib
print(pkg.metrics)

a = pkg.metrics[0]
print(a)

nterms = int(input("Enter terms for Fibonacci Sequence: "))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fib.fibonacci(i))
