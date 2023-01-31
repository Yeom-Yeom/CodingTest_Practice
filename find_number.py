def find_number(num, k):
    for i in str(num):
        if i == str(k):
            return str(num).index(str(k))+1
    return -1

# 다른 사람의 풀이
# def solution(num,k):
#   return -1 if str(k) not in str(num) else str(num.find(str(k))+1