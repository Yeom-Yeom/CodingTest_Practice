def sum_even(n):
    sum = 0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum

# 다른 사람의 풀이
# def solution(n):
#   return sum([i for i in range(2, n+1,2)])
