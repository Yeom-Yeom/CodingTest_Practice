def add_hide_num_1(my_string):
    answer = 0
    for i in my_string:
        print(i)
        if i.isdigit():
            answer+=int(i)
    return answer
    
# 다른 사람의 풀이
# def solution(my_string):
#   return sum(int(i) for i in my_string if i.isdigit())