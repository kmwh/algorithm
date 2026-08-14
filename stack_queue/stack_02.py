def solution(prices):
    st = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while st and prices[st[-1]] > prices[i]:
            answer[st[-1]] = i - st[-1]
            st.pop()
        st.append(i)
    while st:
        answer[st[-1]] = len(prices) - st[-1] - 1
        st.pop()
    return answer