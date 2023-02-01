def cnt_k(i,j,k):
    answer=0
    for n in range(i,j+1):
        answer+=sum([1 for n in list(str(n)) if n == str(k)])
    return answer

# 다른 사람의 풀이
# def solution(i,j,k):
#   return sum(map(lambda v : str(v).count(str(k)),range(1,j+1)))
