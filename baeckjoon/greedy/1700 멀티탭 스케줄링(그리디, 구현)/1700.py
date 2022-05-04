N, K = map(int, input().split())
plugs = list(map(int, input().split()))

multitap = []
result = 0

for i in range(K):
    # 해당 플러그가 멀티탭에 꽂혀있다면 패스
    if plugs[i] in multitap:
        continue

    # 꽂혀있는게 없으면 꽂기
    if len(multitap) < N:
        multitap.append(plugs[i])
        continue

    target_in_multitap = 0
    far_index = 0
    # 멀티탭에 꽂혀있는것 확인
    for multi in multitap:
        # 앞으로 사용할 플러그에 없으면(뽑을 친구)
        if multi not in plugs[i:]:
            target_in_multitap = multi
            break

        # 멀티탭에 꽂혀있는 플러그안에서 가장 나중에 사용되는 플러그를 꽂아준다
        elif plugs[i:].index(multi) > far_index:
            far_index = plugs[i:].index(multi)
            target_in_multitap = multi

    multitap[multitap.index(target_in_multitap)] = plugs[i]
    result += 1
print(result)