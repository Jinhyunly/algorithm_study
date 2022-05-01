n = int(input())
num_list = []
for i in range(n):
    x, y = map(int, input().split())
    num_list.append([x, y])

num_list.sort(key=lambda x: (x[1], x[0]))
for num in num_list:
    print(num[0], num[1], sep=' ')