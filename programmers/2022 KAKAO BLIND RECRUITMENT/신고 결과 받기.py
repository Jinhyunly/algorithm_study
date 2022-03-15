def solution(id_list, report, k):

    answer = [0] * len(id_list)
    reports = {id:0 for id in id_list} # key, value

    # 신고 당한수 (set(report)로 중복제거(한사람이 한사람을 다중 신고한 경우))
    for r in set(report):
        reports[r.split()[1]] += 1
    #print(reports)

    # 신고당한 수가 k번 이상인경우의 사람을 신고한 사람 카운트(메일 수)
    for r in set(report):
        if reports[r.split()[1]] >= k: 
            answer[id_list.index(r.split()[0])] += 1

    return answer