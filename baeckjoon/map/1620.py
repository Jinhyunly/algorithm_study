import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}
for i in range(1, n +1):
    tmp = input()
    dict[i] = tmp
    dict[tmp] = i

for i in range(m):
    target = sys.stdin.readline().rstrip() # \n 포함하고 있기에 해줘야한다
    if target.isdigit():
        print(dict[int(target)])
    else:
        print(dict[target])