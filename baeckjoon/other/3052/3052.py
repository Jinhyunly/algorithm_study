import sys

list = []
for i in range(10):
  list.append(int(sys.stdin.readline()) % 42)

print(len(set(list)))