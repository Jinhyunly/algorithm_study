main_set = {i for i in range(1, 10001)}
not_self_set = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  not_self_set.add(i)

self_set = sorted(main_set - not_self_set)
for num in self_set:
  print(num)