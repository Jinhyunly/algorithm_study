n, m = map(int, input().split())

s = set([input() for _ in range(n)])
cnt = 0
for i in range(m):
    st = input()
    if st in s:
        cnt += 1
print(cnt)