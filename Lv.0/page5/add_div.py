import math

def add_div(numer1, denom1, numer2, denom2):
    top = numer1*denom2 + numer2*denom1
    bottom = denom1*denom2
    n = math.gcd(top, bottom)
    if n == 1:
        return [top, bottom]
    else:
        return [top/n, bottom/n]
    
# 다른 사람의 풀이
# from fractions import Fraction
# def solution(denum1, num1, denum2, num2):
#   answer = Fraction(denum1, num1)+Fraction(denum2, num2)
#   return [answer.numerator, answer.donominator]