import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for i in range(n + 1)]
INF = int(1e9)

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

origin_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_ = origin_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_ = origin_distance[v2] + v2_distance[v1] + v1_distance[n]

min_len = min(v1_, v2_)
if min_len >= INF: #주의하자 이것보다 클수도있다
    print(-1)
else:
    print(min_len)