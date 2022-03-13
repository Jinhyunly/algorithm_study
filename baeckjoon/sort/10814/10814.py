n = int(input())

members = []
for i in range(n):
  age, name = map(str, input().split())
  members.append((int(age), name))

members.sort(key = lambda x : x[0])

for m in members:
  print(m[0], m[1])