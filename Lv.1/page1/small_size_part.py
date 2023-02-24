def small_size_part(t,p):
    answer = 0
    p_len = len(p)
    t_len = len(t)
    p = int(p)
    for i in range(0, t_len+1-p_len):
        if int(t[i:i+p_len]) <= p:
            answer +=1
    return answer

# another solution
# def solution(t,p):
#   return len([t[i:i+len(p)] for i in range(len(t)-len(p)+1) if int(t[i:i+len(p)]) <= int(p)])