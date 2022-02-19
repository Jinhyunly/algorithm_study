import sys
n = int(sys.stdin.readline())

number = list(map(int, input().split()))
number.sort()

result = [[] for _ in range(len(number))]
tmp = 0
for i in range(n):
  tmp += number[i]
  result[i] = tmp

print(sum(result))