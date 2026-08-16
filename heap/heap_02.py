import heapq

def solution(jobs):
    h = [(x[0], x[1], i) for i, x in enumerate(jobs)]
    heapq.heapify(h)
    waiting = []
    
    cur = heapq.heappop(h)
    time = cur[0] + cur[1]
    answer = cur[1]
    while h or waiting:
        while h and h[0][0] <= time:
            temp = heapq.heappop(h)
            heapq.heappush(waiting, (temp[1], temp[0], temp[2]))
        if waiting:
            temp = heapq.heappop(waiting)
            cur = (temp[1], temp[0], temp[2])
        else:
            cur = heapq.heappop(h)
            time = cur[0]
        time += cur[1]
        answer += (time - cur[0])
    
    return answer // len(jobs)