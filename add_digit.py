def add_digit(n):
    result = 0
    while n>0: # n이 0이하로 떨어지지 않으면
        result += n%10 # result에 n을 10으로 나눈 나머지를 더하고 ex) n = 456이라면, result+=6 -> result+=5 -> result+=4
        n = n//10 # n은 n에서 10으로 나눈 몫이 된다. ex) 456//10 = 45 -> 45//10 = 4 -> 4//10 = 0
    return result

# 다른 사람의 풀이
# def solution(n):
#   return sum(int(i) for i in str(n))