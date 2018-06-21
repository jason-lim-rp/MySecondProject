#Datatype

a = 1.0
print (type(a))
a = "Hello"
print (type(a))

c = 1/2
print (c, type(c))
d = 1//2
print (d, type(d))


#Numbers
a = 1
b = 2.0

#Math operation involving a float will get a float
c = a + b
print ("C is : ", c)
print ("C is : ", type(c))

#the datatype of user input will always be String
d = input("Enter a decimal number : ")
print ("datatype of d is ", type(d))

#need to ensure compatible datatype for Math operation
print ("Sum of c and d is ", c + float(d))


#String
a = "Hello"
b = "World"
c = a + " " + b
print (c)

print (c+4)

print (c*3)


#List
a = [4, "abc", 2, 4]
print (a[0])
print (a[3])
print (a[-1])

a = [4, "abc", 2, 4]
print (len(a))
print (a[:2])
print (a[2:])


