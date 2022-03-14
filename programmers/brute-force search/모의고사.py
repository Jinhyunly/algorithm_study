def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    supo_scores = [0 for i in range(3)]
    
    for i in range(len(answers)):
        if supo1[i%len(supo1)] == answers[i]:
            #index를 각 길이로 나눈 나머지와 비교 index = 6이라면 1
            supo_scores[0] += 1
        if supo2[i%len(supo2)] == answers[i]:
            supo_scores[1] += 1
        if supo3[i%len(supo3)] == answers[i]:
            supo_scores[2] += 1
    
    # 가장 많이 맞춘 사람 구하기(0번째 인덱스부터 비교하며 추가하므로 오름차순 정렬이 따로 필요하지 않음)
    for i in range(len(supo_scores)):
        if(supo_scores[i] == max(supo_scores)):
            answer.append(i+1)

    return answer