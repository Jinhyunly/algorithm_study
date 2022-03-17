from collections import deque

# BFS 함수 정의
def bfs(n, graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용  
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복

  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            queue.append(i)
            visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n): # 0 1 2
        if not visited[i]:
            # 정의된 BFS 함수 호출
            bfs(n, computers, i, visited)
            answer += 1
    
    return answer