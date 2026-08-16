import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    num = 0
    count = 0
    while scoville[0] < K and len(scoville) > 1:
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, num)
        count += 1
    if len(scoville) < 2 and scoville[0] < K:
        count = -1
    return count