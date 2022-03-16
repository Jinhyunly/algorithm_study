def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        nums = []
        for i in range(1, int(num**(0.5))+1):
            if num%i == 0:
                nums.append(i)
                if i != num//i:
                    nums.append(num//i)
        if len(nums) % 2 == 0:
            answer += max(nums)
        else:
            answer -= max(nums)
    return answer