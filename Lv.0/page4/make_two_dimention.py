import numpy as np
def make_two_dimention(num_list,n):
    return (np.array(num_list).reshape((len(num_list)//n ,n))).tolist()

# 다른 사람의 풀이
# def solution(num_list, n):
#   answer = []
#   for i in range(0,len(num_list),n):
#        answer.append(num_list[i:i+n])
#   return answer