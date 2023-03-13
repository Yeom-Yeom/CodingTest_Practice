def find_remain_1(n):
    for i in range(2,n):
        if n%i == 1:
            return i
        
# another solution
# def solution(n):
#   return [x for x in range(1,n+1) if n%x==1][0]