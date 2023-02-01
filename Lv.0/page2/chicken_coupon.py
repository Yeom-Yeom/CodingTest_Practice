def chicken_coupon(chicken):
    answer = 0
    while chicken>=10:
        div = chicken//10
        mod = chicken %10
        answer+=div
        chicken = div+mod
    return answer

# 다른 사람의 풀이
# def solution(chicken):
#   return int(chicken*0.1111111111)