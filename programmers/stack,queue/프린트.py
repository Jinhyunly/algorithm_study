def solution(priorities, location):
    answer = 0
    
    arr_index = [x for x in range(len(priorities))]
    arr_value = priorities.copy()
    
    priorities.sort(reverse=True)
    i = 0
    
    while arr_value != priorities: #내림차순 정렬이 될때까지
        if arr_value[i] < max(arr_value[i+1:]): # arr_value[i]가 최대값이 아닐때
            arr_value.append(arr_value.pop(i)) 
            arr_index.append(arr_index.pop(i))
        else: # arr_value[i]가 최대값일 때
            i += 1
    
    # 내림차순 정렬이 되었을 때의 정렬된 인덱스 리스트의 인덱스 값을 구해서 몇번째인지를 알려준다
    answer = arr_index.index(location) + 1
    
    return answer