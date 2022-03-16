def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    
    # 큐를 이용해 days를 이용한 계산식에서 pop을 결정
    while len(progresses) != 0:
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            # days가 증가
            if count > 0:
                answer.append(count)
                count = 0
            days += 1

    answer.append(count)


    return answer