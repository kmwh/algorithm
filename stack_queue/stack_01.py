def solution(s):
    st = []
    for i in s:
        if i == ')' and st and st[-1] == '(':
            st.pop()
        else:
            st.append(i)
    
    return len(st) == 0