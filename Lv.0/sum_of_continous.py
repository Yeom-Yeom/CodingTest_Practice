def sum_of_continous(num, total):
    answer = []
    for i in range(num): # 연속된 수 만큼
        if num%2 == 0:
            answer.append(total//num-num//2-1+i) # total에서 num을 나눈 몫이 배열의 중간 값이 됨
            # 그 중간 값에서 짝수인 경우 좌측의 갯수가 우측의 갯수보다 -1개             
        else:
             answer.append(total//num-num//2+i) # 중간 값이 홀수인 경우, 그 수를 기준으로 양쪽으로 수를 동일한 갯수를 넣어줌.
    return answer

# def solution(num,total):
#     return [(total - (num * (num-1)//2))//num+i for i in range(num)]