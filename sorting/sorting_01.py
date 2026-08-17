def solution(array, commands):
    answer = []
    for i in commands:
        sl = sorted(array[(i[0]-1):i[1]])
        answer.append(sl[i[2] - 1])
    return answer