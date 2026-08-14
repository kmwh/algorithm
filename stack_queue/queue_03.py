from collections import deque

def solution(priorities, location):
    qu = deque(priorities)
    count = 0
    while qu:
        cur = qu.popleft()
        location -= 1
        if not qu or (max(qu) <= cur):
            count += 1
            if location == -1:
                break
        else :
            qu.append(cur)
            if location == -1:
                location = len(qu) - 1
        
    return count