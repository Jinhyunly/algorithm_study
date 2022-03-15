import collections

numbers = [1,2,3,4,6,7,8,0]
origin_nums= [0,1,2,3,4,5,6,7,8,9]

answer = collections.Counter(origin_nums) - collections.Counter(numbers)

print(sum(list(answer.keys())))

# 다른 사람 풀이
# def solution(numbers):
#     return 45 - sum(numbers)