import sys

n = int(sys.stdin.readline())

arr = []
for i in str(n):
  arr.append(int(i))

arr.sort(reverse = True)
for i in arr:
  print(i, end = '')


#################################
# 리펙토링

nums = input()
nums = [int(n) for n in nums]

ordered_nums = sorted(nums, reverse = True)

for n in ordered_nums:
  print(n, end='')