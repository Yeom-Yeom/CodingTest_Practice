def calc_shortfall(price,money,count):
    tmp = 0
    for c in range(1,count+1):
        tmp += (c*price)
    if tmp < money:
        return 0
    return tmp-money

# another solution
# def solution(price,money,count):
#   return max(0,price*(count+1)*count//2-money)