n = input()
f = int(input())

tmp = n[:-2] + "00"
tmp2 = n[:-2] + "99"
result = ""

for num in range(int(tmp), int(tmp2)+1):
  if num%f == 0:
    result = str(num)[-2:]
    break

print(result)