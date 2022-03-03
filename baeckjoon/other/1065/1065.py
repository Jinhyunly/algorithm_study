import sys

n = int(sys.stdin.readline())

def hansu(n):
  hansu_cnt = 0
  for num in range(1, n+1):
    num_list = list(map(int, str(num)))
    if num < 100:
      hansu_cnt += 1
    else:
      if num_list[0]- num_list[1] == num_list[1] - num_list[2]:
        hansu_cnt += 1
  return hansu_cnt

print(hansu(n))