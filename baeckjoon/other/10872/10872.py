import math
import sys

n = int(sys.stdin.readline())
print(math.factorial(n))


--------------------------------

import sys

n = int(sys.stdin.readline())

def fac(n):
  result = 1
  for i in range(1, n+1):
    result = result * i
  return result
  
print(fac(n))