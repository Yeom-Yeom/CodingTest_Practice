def choice_n_multiple(n, numlist):
    answer = []
    for i in numlist: # numlist의 원소들 중에서
        if i%n==0: # 하나씩 비교, n으로 나누어 떨어지면 n의 배수
            answer.append(i) # answer 배열에 추가.
        else:
            continue
    return answer

# 다른 사람의 풀이
# def solution(n, numlist):
#   return list(filter(lambda v : v%n==0, numlist))