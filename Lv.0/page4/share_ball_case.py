from math import factorial
def share_ball_case(balls, share):
    return factorial(balls)//(factorial(balls-share)*factorial(share))

# 다른 사람의 풀이
# import math
# def solution(balls,share):
#   return math.comb(balls,share) <- math.comb : combination(조합)