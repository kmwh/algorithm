from collections import deque

def solution(bridge_length, weight, truck_weights):
    b = deque([0] * bridge_length)
    t = deque(truck_weights)
    time = 0
    cur = 0
    
    while t:
        time += 1
        cur -= b.popleft()
        if (cur + t[0]) <= weight:
            cur += t[0]
            b.append(t.popleft())
        else:
            b.append(0)
    time += bridge_length
    return time