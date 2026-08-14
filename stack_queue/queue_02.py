from collections import deque

def solution(progresses, speeds):
    p_qu = deque(progresses)
    s_qu = deque(speeds)
    answer = []
    
    while p_qu:
        if p_qu[0] >= 100:
            count = 0
            while p_qu and p_qu[0] >= 100:
                count += 1
                p_qu.popleft()
                s_qu.popleft()
            answer.append(count)
        for i in range(len(p_qu)):
            p_qu[i] += s_qu[i]
    
    return answer