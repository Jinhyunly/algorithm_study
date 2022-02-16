n = int(input())

arr = []
for i in range(n):
  arr.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  if x<0 or y<0 or x>=n or y>=n:
    return False
  if arr[x][y] == 0:
    return False
  
  if arr[x][y] == 1:
    global count
    count += 1
    arr[x][y] = 0
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

result = 0
count = 0
num = []
for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      num.append(count)
      result += 1
      count = 0
num.sort()
print(result)
for i in range(len(num)):
  print(num[i])