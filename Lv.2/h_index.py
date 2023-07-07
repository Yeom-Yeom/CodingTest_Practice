def h_index(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

print(h_index([3,0,6,1,5]))


# another solution
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min,enumerate(citations,start=1)))
#     return answer