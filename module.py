#import primeModule
#print(dir(primeModule)) #Print all functions of a module

#import primeModule as pr #import as alias
#pr.PrimeTo(100)

from primeModule import PrimeTo #Import a single function from a module
PrimeTo(100)
