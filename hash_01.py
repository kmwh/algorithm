from collections import Counter

def solution(participant, completion):
    par_c = Counter(participant)
    com_c = Counter(completion)
    answer = list((par_c - com_c).keys())[0]
    return answer