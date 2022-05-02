N, M = map(int, input().split())
s = []

def BackT(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N + 1):
        if i in s:
            continue

        s.append(i)
        BackT(i + 1)
        s.pop()

BackT(1)