n, m = map(int, input().split())

solve = []
def BackT():
    if len(solve) == m:
        print(' '.join(map(str, solve)))
        return

    for i in range(1, n+1):
        solve.append(i)
        BackT()
        solve.pop()
BackT()