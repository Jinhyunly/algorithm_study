import sys

word = sys.stdin.readline().rstrip()

dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

result = 0
for w in word:
  for i in range(0, len(dial)):
    if w in dial[i]:
      result += i+3

print(result)