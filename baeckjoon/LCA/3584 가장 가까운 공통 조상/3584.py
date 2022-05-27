import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    p_list = [0 for i in range(N + 1)]

    for j in range(N - 1):
        a, b = map(int, input().split())
        p_list[b] = a  # 각 자식노드의 인덱스에 부모의 값으로 설정

    a, b = map(int, input().split())

    # 자기 자신의 값을 첫 값으로 설정
    a_parent = [a]  # 16
    b_parent = [b]  # 7

    # 각 부모의 노드를 리스트에 추가
    while p_list[a]:
        a_parent.append(p_list[a])
        a = p_list[a]

    while p_list[b]:
        b_parent.append(p_list[b])
        b = p_list[b]

    # 루트노드부터 비교를 위해 (같은 깊이)
    a_level = len(a_parent) - 1
    b_level = len(b_parent) - 1

    while a_parent[a_level] == b_parent[b_level]:
        a_level -= 1
        b_level -= 1

    # a_parent = [16, 10, 4, 8]
    # b_parent = [7, 6, 4, 8]
    # 뒤의 루트노드부터 계산하여 4가 출력되로록 한다
    print(a_parent[a_level + 1])
