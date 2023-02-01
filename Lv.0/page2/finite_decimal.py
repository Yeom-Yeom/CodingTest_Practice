from math import gcd # gcd(Greatest Common Divisor = 최대공약수)를 사용
def finite_decimal(a,b):
    b //=gcd(a,b) # a와 b의 최대 공약수 만큼 분모 b를 나눈다.
    while b%2 ==0: # b가 2로 나누어 떨어지지 않을 때 까지 2로 나눈다.
        b//=2
    while b%5==0: # b가 5로 나누어 떨어지지 않을 때 까지 5로 나눈다.
        b//=5
    return 1 if b==1 else 2 # 2와 5로 나누었을 때 다 나누어져 1이 남는다면 유한소수, 아니라면 무한소수.