import sys

n = int(sys.stdin.readline())

for i in range(n):
  strOX = sys.stdin.readline().rstrip()
  count = 0
  result = 0
  for ox in strOX:
    if ox == 'O':
      count += 1
    else:
      count = 0
    result += count
  
  print(result)