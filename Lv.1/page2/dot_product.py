def dot_product(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# another solution
# def solution(a,b):
#   return sum([x*y] for x,y in zip(a,b))