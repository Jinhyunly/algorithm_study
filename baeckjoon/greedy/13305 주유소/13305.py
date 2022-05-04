n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
result = 0
good_cost = costs[0]

for i in range(n-1): # 마지막 주유는 안함(도로 인덱스도 생각)
    if costs[i] < good_cost:
        good_cost = costs[i]
    result += good_cost * roads[i]

print(result)