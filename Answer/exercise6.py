import Day2Resource.primenumbergenerator
import time

t1 = time.time()

for i in Day2Resource.primenumbergenerator.prime(end=10000):
  print(i)

t2 = time.time()

print ("total time was %f" % float(t2-t1) , " sec")

