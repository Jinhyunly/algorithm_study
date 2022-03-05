import sys

n = int(sys.stdin.readline())

list = []

for i in range(n):
  n, m = map(str, sys.stdin.readline().split())
  tmp = ""
  for a in m:
    for j in range(int(n)):
      tmp += a
  list.append(tmp)

for l in list:
  print(l)