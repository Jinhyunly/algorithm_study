n, m = map(int, input().split())

solve = []

def BackT(t):
    if len(solve) == m:
        print(' '.join(map(str, solve)))
        return

    for i in range(t, n+1):
        solve.append(i)
        BackT(i)
        solve.pop()

BackT(1)