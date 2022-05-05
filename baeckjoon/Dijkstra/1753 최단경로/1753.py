# 정점의수, 간선의 개수
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(v + 1)]
distance = [INF] * (v + 1)

for i in range(e):
    u, v1, w = map(int, input().split())  # u에서 v로가는 w가중치
    graph[u].append((v1, w))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        #가장 최단 거리가 짧은 노드에 정보 꺼내기
        dist, now = heapq.heappop(queue)

        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])