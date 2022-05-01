import sys
n = int(sys.stdin.readline())

list = []
for i in range(n):
  list.append(int(sys.stdin.readline()))

list.sort()

for i in range(len(list)):
  print(list[i])