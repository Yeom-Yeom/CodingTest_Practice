def lifeboat(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people)-1
    while a <= b:
        answer+=1
        if people[b] + people[a] <= limit:
            a +=1
        b -=1
    return answer