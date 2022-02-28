import sys

result = list(str(int(sys.stdin.readline()) * int(sys.stdin.readline()) * int(sys.stdin.readline())))

for i in range(10):
  print(result.count(str(i)))