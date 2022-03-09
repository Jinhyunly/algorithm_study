def solution(participant, completion):
    answer = ''
    isFind = False
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            isFind = True
            break

    if not isFind:
        answer = participant[-1]

    return answer

###########################################################
# 다른사람 코드
#import collections

#def solution(participant, completion):
#    answer = collections.Counter(participant) - collections.Counter(completion)
#    return list(answer.keys())[0]

