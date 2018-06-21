#default parameters

def addNum(a = 2, b = 5):
    return a + b




#lambda functions

def make_adder(n):
    return lambda x: x + n

adder2 = make_adder(2)
val = adder2(5)
print (val)

adder3 = make_adder(4)
val = adder3(5)
print (val)


import math

def square_root(x):
    return math.sqrt(x)

result = square_root(4)
print (result)

square_root = lambda x: math.sqrt(x)

result = square_root(4)
print (result)

