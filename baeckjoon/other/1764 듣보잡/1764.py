n, m = map(int, input().split())

a = set()
b = set()
for i in range(n):
    a.add(input())

for i in range(m):
    b.add(input())

tmp = sorted(list(a & b))
print(len(tmp))
for i in tmp:
    print(i)