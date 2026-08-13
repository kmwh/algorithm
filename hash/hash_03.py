def solution(phone_book):
    answer = True
    s = set(phone_book)
    for i in phone_book:
        for j in range(1, len(i)):
            if i[:j] in s:
                answer = False
                break
        if not answer:
            break
    return answer