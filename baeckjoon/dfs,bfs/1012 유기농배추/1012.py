from collections import deque

t = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def Bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for i in range(t):
    m, n, k = map(int, input().split()) #가로, 세로 배추개수

    graph = [[0] * (m) for i in range(n)]
    
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1 #

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                Bfs(i,j)
                count += 1

    print(count)