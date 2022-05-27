from itertools import permutations

n = int(input())
k = int(input())

cards = [input() for _ in range(n)]

ans = set()
for per in permutations(cards, k):
    ans.add(''.join(per))

print(len(ans))