import sys

n = int(sys.stdin.readline())

for i in range(n):
  strTmp = sys.stdin.readline().rstrip()
  stack = []
  
  for tmp in strTmp:
    if tmp == "(":
      stack.append(tmp)
    elif tmp == ")":
      if stack and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(tmp)
        break

  if not stack: #스텍에 값이 존재하지 않을 때
    print("YES")
  else:
    print("NO")