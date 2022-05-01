import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
num_rank_list = sorted(list(set(num_list)))

dic = {num_rank_list[i] : i for i in range(len(num_rank_list))}
for num in num_list:
    print(dic[num], end=' ')