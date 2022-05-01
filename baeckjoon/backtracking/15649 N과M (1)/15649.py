N, M = map(int, input().split())

solve = []
visited = [False] * (N+1) # 방문체크 할 리스트

def BackT():
    # print(solve)
    if len(solve) == M:
        print(*solve)
        return

    for i in range(1, N+1): # 예) 길이가2라면 첫번째 스택에 담기고 두번째 인수를 담는다(다시 1부터 됨)
        if visited[i]: # 이미 방문했으면 건너뜀
            continue
        #방문 안했으면 방문체크 후, 출력 리스트에 넣음
        visited[i] = True
        solve.append(i)
        BackT() # 함수 다시 호출
        # print(solve)
        solve.pop() # 원상복귀 과정 필요
        # print(solve)
        visited[i] = False
BackT()