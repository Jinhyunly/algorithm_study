from collections import deque

n = int(input())

for _ in range(n):
    num_len, target_idx = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idx_list = [x for x in range(num_len)]
    idx_list[target_idx] = 'target'

    idx = 0

    while queue:
        if queue[0] == max(queue):
            idx += 1
            if idx_list[0] == 'target':
                print(idx)
                
            queue.popleft()
            idx_list.pop(0)

        else:
            queue.append(queue.popleft())
            idx_list.append(idx_list.pop(0))
