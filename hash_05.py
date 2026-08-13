from collections import defaultdict

def solution(genres, plays):
    d = defaultdict(list)
    for i in range(len(genres)):
        d[genres[i]].append((plays[i], i))
    for i in d.keys():
        d[i] = sorted(d[i], key = lambda x : (-x[0], x[1]))
    sorted_l = sorted(d.items(), key = lambda x : sum(t[0] for t in x[1]), reverse = True)
    answer = []
    for i in sorted_l:
        answer.extend([x[1] for x in i[1][:2]])
    return answer