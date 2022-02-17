from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
arr = deque([])

for i in range(n):
  arr.append(i+1)

print('<', end='')
while arr:
  for i in range(1, k):
    arr.append(arr.popleft())
  print(arr.popleft(), end='')
  if arr:
    print('', end=', ')
print(">")