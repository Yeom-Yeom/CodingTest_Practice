def long_jump(n):
    if n<3:
        return n
    d = [0]*(n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3,n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n]%1234567

# another solution
# def solution(n):
#     a,b = 0.1
#     for i in range(1,n):
#         a,b = b, a+b
#     return b