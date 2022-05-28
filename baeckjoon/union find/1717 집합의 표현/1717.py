import sys
sys.setrecursionlimit(100000) # n의 범위
input = sys.stdin.readline

n, m = map(int, input().split())

# 자기 자신을 부모로 설정
p_list = [i for i in range(n+1)]

# 루트 노드 찾는 함수
def find(a):
    if a == p_list[a]:  #자기 자신이 루트 노드이면 a 반환
        return a
    p_list[a] = find(p_list[a]) # a의 루트 노드 찾기 및 부모 테이블 갱신
    return p_list[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a, b):
    a = find(a) # a의 루트 노드 찾기
    b = find(b) # b의 루트 노드 찾기

    # a와 b의 루트 노드가 다르면 두 집합을 합치기
    if a < b:
        p_list[b] = a
    else:
        p_list[a] = b


for i in range(m):
    o, a, b = map(int, input().split())
    if o: # o가 1일때, 각 루트 노드를 찾아 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b) # o가 0일때, 두 원소가 포함되어 있는 집합을 합치기