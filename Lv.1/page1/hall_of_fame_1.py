from heapq import heappop,heappush

def hall_of_fame_1(k, score):
    answer = []
    heap = []
    for s in score:
        heappush(heap,s)
        if len(heap)>k:
            heappop(heap)
        answer.append(heap[0])
    return answer

# another solution
# def solution(k,score):
#   q = []
#   answer = []
#   for s in score:
#       q.append(s)
#       if len(q)>k:
#           q.remove(min(q))
#       answer.append(min(q))
#   return answer