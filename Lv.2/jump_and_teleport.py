def jump_and_teleport(n):
    answer = 0
    while n > 0:
        answer += n%2
        n //= 2
    return answer


# another solution
# def solution(n):
#     return bin(n).count('1')