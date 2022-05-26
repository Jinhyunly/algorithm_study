import sys

input = sys.stdin.readline
n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

card_list.sort()

# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card_list, check_list[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
