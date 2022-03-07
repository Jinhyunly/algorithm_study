import sys
n = int(sys.stdin.readline())

result = n

for i in range(n):
  word = sys.stdin.readline().rstrip()
  for j in range(0, len(word)-1):
    if word[j] == word[j+1]:
      pass
    else:
      if word[j] in word[j+1:]:
        result -= 1
        break

print(result)