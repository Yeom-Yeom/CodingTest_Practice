import itertools
def cnt_sum_of_consecutive_subsequences(elements):
    answer = 0
    tmp = []
    for i in range(1,len(elements)+1):
        arr = itertools.combinations(elements,i)
        for j in arr:
            if sum(j) not in tmp:
                tmp.append(sum(j))
    print(tmp)
    return len(tmp)

print(cnt_sum_of_consecutive_subsequences([7,9,1,1,4]))