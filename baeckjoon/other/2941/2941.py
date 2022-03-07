import sys

word = sys.stdin.readline().rstrip()

arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for ar in arr:
  word = word.replace(ar, "*")

print(len(word))