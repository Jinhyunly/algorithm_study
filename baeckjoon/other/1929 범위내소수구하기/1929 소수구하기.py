import sys
import math

m, n = map(int, sys.stdin.readline().split())

def is_prime_num(n):
  if n==1:
    return False
  else:
    for i in range(2, int(math.sqrt(n))+1):
      if n%i == 0:
        return False
    return True

for i in range(m, n+1):
  if is_prime_num(i):
    print(i)