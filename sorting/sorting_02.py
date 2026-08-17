from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    str_nums = list(map(str, numbers))
    sl = sorted(str_nums, key=cmp_to_key(compare))
    answer = "".join(sl)
    if answer[0] == '0':
        answer = '0'
    return answer