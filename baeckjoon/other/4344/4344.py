import sys

n = int(sys.stdin.readline())

for i in range(n):
  tmp= list(map(int, sys.stdin.readline().split()))
  students = tmp[0]
  avg = (sum(tmp)-tmp[0])/(len(tmp)-1)
  count = 0
  for i in range(1, len(tmp)):
    if tmp[i] > avg:
      count += 1
  print("{:.3f}%".format(count/(len(tmp)-1)*100))