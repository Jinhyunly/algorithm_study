import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

result = [0 for i in range(len(b))]

for idx in range(len(b)):
  start = 0
  end = len(a) - 1
  
  while(start<=end):
    mid = (start + end) // 2
    
    if a[mid] == b[idx]:
      result[idx] = 1
      break
    elif a[mid] > b[idx]:
      end = mid - 1
    else:
      start = mid + 1

for i in result:
  print(i)
