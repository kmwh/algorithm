from collections import defaultdict

def solution(clothes):
    c_dict = defaultdict(list)
    for c in clothes:
        c_dict[c[1]].append(c[0])
    answer = 1
    for i in c_dict.keys():
        answer *= (len(c_dict[i]) + 1)
        
    return answer - 1