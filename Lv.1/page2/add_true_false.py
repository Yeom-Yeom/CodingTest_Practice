def add_true_false(absolutes,signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 0:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer

# anther solution
# def solution(absolutes, signs):
#   return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes,signs))

