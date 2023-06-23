def fibonacci_num(n):
    answer = []
    for i in range(n+1):
        if i==0 or i == 1:
            answer.append(i)
        else:
            f = answer[i-1]+answer[i-2]
            answer.append(f%1234567)
    return answer[-1]

# another solution
# def solution(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b, (a+b)%1234567
#     return a