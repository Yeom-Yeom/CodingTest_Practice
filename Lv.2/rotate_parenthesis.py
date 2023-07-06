def rotate_parenthesis(s):
    answer = 0 
    temp = list(s)

    for _ in range(len(s)):

        st = []
        for i in range(len(temp)):
            if len(st) > 0:
                if st[-1] == '[' and temp[i] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[i] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            if len(st) == 0:
                answer += 1
            temp.append(temp.pop(0))
    return answer

# another solution
# from collections import deque
# def check(s):
#     while True:
#         if "()" in s: s=s.replace("()","")
#         elif "{}" in s : s=s.replace("{}","")
#         elif "[]" in s : s=s.replace("[]","")
#         else: return False if s else True

# def solution(s):
#     ans = 0
#     que = deque(s)

#     for i in range(len(s)):
#         if check(''.join(que)): ans+=1
#         que.rotate(-1)
#     return ans