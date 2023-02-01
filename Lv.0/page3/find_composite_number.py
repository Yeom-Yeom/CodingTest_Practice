def find_composite_number(n):
    num = []
    answer = 0
    
    for i in range(2,n+1):
        for j in range(1, i+1):
            if i%j==0:
                num.append(i)
        if num.count(i)>=3:
            answer+=1
    return answer

# 다른 사람 풀이
# def solution(n):
#   output = 0
#   for i in range(4, n+1):
#       for j in range(2, int(i**0.5)+1):
#           if i%j==0:
#               output+=1
#               break
#   return output