def failure(N, stages):
    result = {}
    denom = len(stages)
    for stage in range(1,N+1):
        if denom != 0:
            count = stages.count(stage)
            result[stage] = count/denom
            denom -= count
        else:
            result[stage] = 0
    return sorted(result,key=lambda x : result[x], reverse=True)

# another solution
# def solution(N, stages):
#   answer = [], fail = [], info = [0]*(N+2)
#   for stage in stages:
#       info[stage] +=1
#   for i in rnage(N):
#       be = sum(info[(i+1):])
#       yet = info[i+1]
#       if be == 0:
#           fail.append((str(i+1),0))
#       else:
#           fail.append((str(i+1),yet/be))
#   for item in sorted(fail,key=lambda x: x[1], reverse=True):
#       answer.append(int(item[0]))
#   return answer