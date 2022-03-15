def solution(s):
    dic = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in range(len(dic)):
        if dic[i] in s:
            s = s.replace(dic[i],str(i))

    return int(s)