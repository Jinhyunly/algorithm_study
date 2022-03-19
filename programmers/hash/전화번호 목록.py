def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
    
    return answer


# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if len(phone_book[i]) < len(phone_book[i+1]):
#             if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 break
#     return answer