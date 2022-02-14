n, k = map(int, input().split())

money = []

for i in range(n):
  money.append(int(input()))

money.sort(reverse=True)

count = 0
for m in money:
  if k // m > 0:
    count += k//m
    k %= m
  if k == 0:
    break  

print(count)