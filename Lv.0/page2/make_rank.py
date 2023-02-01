def make_rank(score):
    answer = []
    li = []
    for i in score:
        li.append(sum(i)/len(i))
    sort_arr = sorted(li,reverse=True)
    for i in li:
        answer.append(sort_arr.index(i)+1)
    return answer

# 다른 사람 풀이
# def solution(score):
#   a = sorted([sum(i) for i in score],reverse = True)
#   return [a.index(sum(i))+1 for i in score]