n = int(input())

data = list(map(int, input().split()))
m = int(input())

#오름차순 정렬
data.sort()

count = 0

start = 0
end = n-1

while start < end:
  tmp = data[start] + data[end]

  if tmp == m:
    count += 1
    start += 1
  elif tmp < m:
    #tmp가 m보다 작을 경우는 두 값의 합이 부족하므로 start를 1 증가시킴(오름차순 정렬)
    start += 1
  else:
    #tmp m보다 클 경우, end를 1 감소시킨다. (오름차순 정렬이기 때문에 한칸 내림)
    end -=1

print(count)