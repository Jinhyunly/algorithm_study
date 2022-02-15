from collections import deque

#정점개수, 간선개수, 정점번호
n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
  x, y = list(map(int, input().split()))
  graph[x].append(y)
  graph[y].append(x)

for i in range(n+1):
  graph[i].sort()

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(graph2, v, visited):
  visited[v] = True
  print(v, end= ' ')
  for i in graph2[v]:
    if not visited[i]:
      dfs(graph2, i, visited)

def bfs(graph2, v, visited):
  queue = deque([v])
  bfs_visited[v] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph2[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)