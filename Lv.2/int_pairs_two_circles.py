def int_pairs_two_circles(r1,r2):
    answer = 0
    minY, maxY = r1,r2
    for x in range(0,r2):
        while r2**2 < maxY**2 + x**2:
            maxY -=1
        while minY-1 and r1**2 <= (minY-1)**2 + x**2:
            minY -=1
        answer +=(maxY-minY)+1
    return answer*4


# another solution
#
# from math import sqrt
# def solution(r1, r2):
#   quar = 0
#   for i in range(0,r1):
#       quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 -1))
#   for i in range(r1,r2):
#       quar += int(sqrt(r2**2 - i**2))
#   return quar * 4