from itertools import permutations
import math

def solution(numbers):
    answer = []
    
    nums = [n for n in numbers] # 한자리씩 배열에 담는다

    perNums = []

    # 순열로 모든 경우의 수 (1자리 소수.., 전체가 소수인 수)
    for i in range(1, len(numbers)+1):
      # print(list(permutations(nums,i)))
      perNums += list(permutations(nums,i))

    new_nums = [int(("").join(p)) for p in perNums]
    # print(new_nums) # [1,7,17,71]

    for num in new_nums:
        if num < 2:
            continue

        sosuFlg = True

        #2부터 제곱근까지
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sosuFlg = False
                break
        if sosuFlg:
            answer.append(num)
            
    return len(set(answer))