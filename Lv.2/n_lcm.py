import math
def n_lcm(arr):
    answer = arr[0]
    for i in range(len(arr)-1):
        answer = (answer*arr[i+1])/math.gcd(int(answer),arr[i+1])
    return int(answer)

print(n_lcm([2,6,8,14]))

# another solution
# from fractions import gcd
# def solution(arr):
#     answer = arr[0]
#     for a in arr:
#         answer = a * answer / gcd(a,answer)
#     return answer