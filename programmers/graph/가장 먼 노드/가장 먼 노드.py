from collections import deque

def solution(n, edge):
    answer = 0 
    distance = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    
    queue = deque()
    queue.append(1)
    distance[1] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]: 
            if distance[i] == 0: # 1 -> 2,3,4
                distance[i] += distance[now] + 1
                queue.append(i)
    
    max_num = max(distance)
    count = 0
    for dist in distance:
        if dist == max_num:
            count += 1
    answer = count
    
    return answer