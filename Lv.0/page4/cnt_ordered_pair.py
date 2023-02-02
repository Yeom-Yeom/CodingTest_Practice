def cnt_ordered_pair(n):
    answer = 0 
    for i in range(1,n+1):
        if n%i==0 : 
            answer+=1
    return answer

# 다른 사람의 풀이
# def solution(n):
#   return len(list(filter(lmabda v : n%(v+1)==0,range(n))))
