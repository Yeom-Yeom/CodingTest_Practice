def fruit_seller(k,m,score):
    answer = 0
    if m > len(score):
        answer=0
    else:
        sort_score = sorted(score,reverse=True)
        sort_slice = [sort_score[i:i+m] for i in range(0,len(sort_score),m)
                      if len(sort_score[i:i+m])==m]
        for i in sort_slice:
            answer+= min(i)*len(i)

    return answer

# another soluiton
# def solution(k,m,score):
#   return sum(sorted(score)[len(score)%m::m])*m