import sys

str = sys.stdin.readline().rstrip()
strList = str.split('-')

num = []
for str in strList: 
  num.append(sum(list((map(int,str.split('+'))))))

result = int(num[0])
if len(num) > 1:
  for i in range(1, len(num)):
    result -= int(num[i])

print(result)