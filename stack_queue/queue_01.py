from collections import deque

def solution(arr):
    q = deque(arr)
    answer = []
    while q:
        val = q.popleft()
        if not answer or answer[-1] != val:
            answer.append(val)
    return answer