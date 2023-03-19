import itertools
def choice_and_add_two_num(numbers):
    ncr = list(itertools.combinations(numbers,2))
    answer = []
    for i in ncr:
        answer.append(i[0]+i[1])
    answer = sorted(list(set(answer)))
    return answer
