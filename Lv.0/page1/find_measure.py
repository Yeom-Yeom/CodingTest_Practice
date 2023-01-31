def find_measure(n):
    answer = []
    i=1
    while i<=n:
        if n%i==0:
            answer.append(i)
        i+=1
    return answer

# 다른 사람의 풀이
# def solution(n):
#   return [i for i in range(1,n+1) if n%1 ==0]