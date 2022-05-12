import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_num_list = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        sum_num_list[i] = num_list[i]
    else:
        sum_num_list[i] = sum_num_list[i-1] + num_list[i]

for i in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(sum_num_list[j-1])
    else:
        print(sum_num_list[j-1] - sum_num_list[i-2])