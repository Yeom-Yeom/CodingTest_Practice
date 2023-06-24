def english_ending(n, words):
    answer = [0,0]

    cnt = 0
    checks = []
    checks.append(words[0])
    for i in range(1, len(words)):
        cnt+=1
        if words[i] not in checks and list(words[i-1])[-1] == list(words[i])[0] :
            checks.append(words[i])
        else:
            answer[0] = cnt%n+1
            answer[1] = cnt//n+1
            break
    return answer

# another solution
# def solution(n,words):
#     for i in range(1, len(words)):
#         if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
#             return [(i%n)+1, (i//n)+1]
#         else:
#             return [0,0]