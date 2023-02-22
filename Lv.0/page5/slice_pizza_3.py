def slice_pizza_3(slice, n):
    for i in range(1,101):
        if slice*i >= n:
            return i
# 다른 사람의 풀이
# def solution(slice, n):
#   return ((n-1)//slice)+1
        