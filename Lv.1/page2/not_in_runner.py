def not_in_runner(participant, completion):
    hashDict = {}
    sumHash = 0

    for p in participant:
        hashDict[hash(p)] = p
        sumHash += hash(p)
    for c in completion : 
        sumHash -= hash(c)
    return hashDict[sumHash]
print(not_in_runner(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
