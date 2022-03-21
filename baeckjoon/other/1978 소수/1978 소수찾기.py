import math
n = int(input())
arr = list(map(int, input().split()))

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
  # 2부터 x의 제곱근(루트)까지의 모든 수를 확인
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False # 소수아님
  return True # 소수

count = 0
for num in arr:
  if num <= 1:
    continue
  if True == is_prime_number(num):
    count+=1

print(count)