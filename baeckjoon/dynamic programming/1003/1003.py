t = int(input())

for i in range(t):
  n = int(input())
  # 1 0 1 1 2 3 5 8 ..
  zero = [1,0,1]
  # 0 1 1 2 3 5 8 13 ..
  one = [0,1,1]
  if n>=3:
    for i in range(3, n+1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])
  print(zero[n], one[n])