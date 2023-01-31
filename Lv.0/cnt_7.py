def cnt_7(array):
    answer = 0
    for i in array: # 만약 array = [7,17,77]이라면 i는 7,17,77이 됨.
        for j in str(i): # 7인경우 j는 7, 17인 경우 1,7
            if '7' in str(j): # j가 7인 경우 answer+=1
                answer+=1
    return answer


# 다른 사람의 풀이
# def solution(array):
#   return str(array).count('7')