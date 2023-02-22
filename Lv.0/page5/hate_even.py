def hate_even(n):
    answer=[]
    for i in range(1, n+1):
        if i%2==1:
            answer.append(i)
    return answer

# 다른 사람의 풀이
# def solution(n):
#   return [i for i in range(1,n+1,2)]