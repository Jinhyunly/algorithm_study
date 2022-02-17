from collections import deque
def solution(numbers, target):
    answer = 0
    # 큐
    queue = deque()
    nL = len(numbers)
    
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
        
    while queue:
        val, idx = queue.popleft()
        idx += 1
        
        if idx < nL:
            queue.append([val + numbers[idx], idx])
            queue.append([val - numbers[idx], idx])
        else:
            if val == target:
                answer +=  1
    return answer