import itertools
def trio(number):
    answer = 0
    tmp = itertools.combinations(number,3)
    for t in tmp:
        if sum(t) == 0:
            answer+=1
    return answer