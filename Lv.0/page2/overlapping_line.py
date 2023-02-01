def overlapping_line(lines):
    answer = 0
    table = [set([]) for i in range(200)] # -100 to 100

    for index, line in enumerate(lines):
        a,b = line
        for i in range(a,b):
            table[i+100].add(index)
    for line in table:
        if len(line)>1:
            answer+=1
    return answer

# 다른 사람의 풀이
# def solution(lines):
#   sets = [set(range(min(l), max(l))) for l in lines]
#   return = len(sets[0]&sets[1] | sets[0]&sets[2] | sets[1]&sets[2])