import sys

word = sys.stdin.readline().rstrip()

alpa = [i for i in range(ord("a"), ord("z")+1)]

result = [-1 for i in range(len(alpa))]

for i in range(0, len(word)):
  for j in range(0, len(alpa)):
    if ord(word[i]) == alpa[j] and result[j] == -1:
      result[j] = i

for r in result:
  print(r, end=' ')

##############################

# find함수 활용

# import sys

# word = sys.stdin.readline().rstrip()

# alpa = [i for i in range(ord("a"), ord("z")+1)]
# for x in alpa:
#   print(word.find(chr(x)), end=' ')