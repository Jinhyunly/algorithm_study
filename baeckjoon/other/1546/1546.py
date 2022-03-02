import sys

n = int(sys.stdin.readline())

scores = list(map(float, sys.stdin.readline().split()))
result = []

for score in scores:
  result.append(score/max(scores)*100)

print(sum(result)/max(result)/len(result)*100)