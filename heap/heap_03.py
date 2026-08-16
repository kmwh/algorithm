import heapq

def solution(operations):
    min_h = []
    max_h = []
    deleted = set()
    for i, s in enumerate(operations):
        ops = s.split()
        n = int(ops[1])
        if ops[0] == "I":
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
        else:
            if n == -1:
                while min_h:
                    temp = heapq.heappop(min_h)
                    if temp[1] in deleted:
                        continue
                    deleted.add(temp[1])
                    break
            if n == 1:
                while max_h:
                    temp = heapq.heappop(max_h)
                    if temp[1] in deleted:
                        continue
                    deleted.add(temp[1])
                    break
    answer = [0, 0]
    if max_h and min_h:
        while max_h:
            temp = heapq.heappop(max_h)
            if temp[1] in deleted:
                continue
            answer[0] = -temp[0]
            break
        while min_h:
            temp = heapq.heappop(min_h)
            if temp[1] in deleted:
                continue
            answer[1] = temp[0]
            break
    return answer