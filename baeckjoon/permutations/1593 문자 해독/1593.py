# 슬라이딩 윈도우
g, s = map(int, input().split())

W = input()
S = input()

answer = 0

# 영 소문자 65 ~ 90
# 영 대문자 97 ~ 122
# 중간꺼 생각 귀찮으니까 65~122라고 지정하기 위해 58 저장공간을 둔다
wa = [0] * 58
sa = [0] * 58

for i in W:
    wa[ord(i) - 65] += 1

# 구간 비교를 시작할 시작점 start와 현재 카운팅한 알파벳 같이 length를 초기화하고 시작한다
start, length = 0, 0

for i in range(s):
    sa[ord(S[i]) - 65] += 1
    length += 1

    if length == g:
        if wa == sa:
            answer += 1
        sa[ord(S[start]) - 65] -= 1  # 길이가 g일때 첫번째 문자를 지우고
        start += 1  # 다음 문자 첫번째 문자를 지우기 위해
        length -= 1  # 첫번째 문자를 지웠으니 길이를 -1 해준다

print(answer)
