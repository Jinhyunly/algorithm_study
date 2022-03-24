n = int(input())

i = 1
num = 1
while True:
  if num >= n:
    print(i)
    break
  num = num + (i * 6)
  i+=1