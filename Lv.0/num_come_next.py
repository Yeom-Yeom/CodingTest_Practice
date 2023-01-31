def num_come_next(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1] : # 등차수열 이라면,
        answer = common[-1]+(common[1]-common[0]) # answer = 마지막 배열의 값에서 공차의 값을 더해줌.
    elif common[1]/common[0] == common[2]/common[1] : # 등비수열 이라면,
        answer = common[-1]*(common[1]/common[0]) # answer = 마지막 배열의 값에서 공비의 값을 곱해줌.
    return answer

# def solution(common):
#     answer = 0
#     a,b,c = common[:3]
#     if (b-a) == (c-b):
#         return common[-1]+(b-a)
#     else:
#         return common[-1]*(b//a)
#     return answer