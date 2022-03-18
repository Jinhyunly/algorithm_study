n = int(input())

mens = []
for i in range(n):
  mens.append(list(map(int, input().split()))) #몸무게 키 리스트로 입력받기

# 완전탐색
for i in mens: 
  rank = 1
  for j in mens:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  print(rank, end=' ') # i 번째 랭크를 출력한다