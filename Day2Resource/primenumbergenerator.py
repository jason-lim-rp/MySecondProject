from math import sqrt

# Primality test
def pt(n):
     for i in range(2,int(sqrt(n))+1):
         if not n % i:
             return False
     return True

def prime(n=2, end=float('inf')):
    while n <= end:
        if pt(n):
            yield n
        n += 1


