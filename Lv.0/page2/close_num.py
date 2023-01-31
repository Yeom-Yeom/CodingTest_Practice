def close_num(array:list,n:int)->int:
    return array[sorted([[index,abs(n-num),num] for index, num in enumerate(array)],key=lambda x: (x[1], x[-1]))[0][0]]

# 다른 사람의 풀이
# def solution(array,n):
#   array.sort(key = lambda x : (abs(x-n),x-n))
#   return array[0]