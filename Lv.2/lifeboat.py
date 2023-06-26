def lifeboat(people, limit):
    answer = 0
    tmp = 0
    people.sort()
    for p in people:
        if tmp > limit:
            return answer
        tmp+=p
        answer+=1