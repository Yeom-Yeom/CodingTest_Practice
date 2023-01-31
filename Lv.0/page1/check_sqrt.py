import math # sqrt 함수를 사용하기 위한 math import
def check_sqrt(n):
    if math.sqrt(n) == int(math.sqrt(n)): # n의 제곱근이 n의 제곱근의 integer 형과 동일하면 그 수는 제곱수.
        return 1
    else :
        return 2

# 다른 사람 풀이
# def solution(n):
#   return 1 if (n**0.5).is_integer() else 2