n = int(input())
time_list = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: (x[1], x[0]))

end = time_list[0][1]
count = 1  # 정렬 후 첫번째 시간은 반드시 카운트 되므로(그리디)
for i in range(1, len(time_list)):
    if time_list[i][0] >= end:
        count += 1
        end = time_list[i][1]
        # print(time_list[i][0], time_list[i][1])

print(count)
