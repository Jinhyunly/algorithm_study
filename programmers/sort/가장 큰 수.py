def solution(numbers):
    arr = sorted(list(map(str, numbers)), reverse=True, key= lambda x:x*3)
    answer = str(int(''.join(arr)))
    
    return answer