import math

n = int(input())
m = int(input())

def is_prime(num):
  if num == 1:
    return False
  else:
    for i in range(2, int(math.sqrt(num))+1):
      if num % i == 0:
        return False
    return True

arr = []
for i in range(n, m+1):
  if is_prime(i):
    arr.append(i)

if len(arr) != 0:
  print(sum(arr))
  print(min(arr))
else:
  print(-1)