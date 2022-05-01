import sys
from collections import Counter

n = int(sys.stdin.readline())

num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

print(round(sum(num_list) / n))
print(num_list[n // 2])

cnt_num_list = Counter(num_list).most_common()
# 숫자는 오름차순 갯수는 내림차순 정렬

if len(cnt_num_list) > 1 and cnt_num_list[0][1] == cnt_num_list[1][1]:
    print(cnt_num_list[1][0])
else:
    print(cnt_num_list[0][0])

print(max(num_list) - min(num_list))
