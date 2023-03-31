def score_memory(name, yearning, photo):
    score = dict()
    result = [0]*len(photo)
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    print(score)
    for i in range(len(photo)):
        for j in photo[i]:
            for k in score.keys():
                if j == k:
                    result[i] += score[k]
    return result


# print(score_memory(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))

# another solution
# def solution(name, yearning, photo):
#   return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]
