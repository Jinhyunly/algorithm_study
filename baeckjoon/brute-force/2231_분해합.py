n = int(input())

min_num = 0
for i in range(1, n+1):
  if n == (i + sum(map(int, str(i)))): # 숫자 + 각 자리수 합
    min_num = i
    break;

print(min_num)