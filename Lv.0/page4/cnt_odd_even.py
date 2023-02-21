def cnt_odd_even(num_list):
    answer=[0,0]
    for i in num_list:
        if i%2==1:
            answer[1]+=1
        else:
            answer[0]+=1
    return answer

# 다른 사람의 풀이
# def solution(num_list):
#   answer = [0,0]
#   for n in num_list;
#       answer[n%2]+=1
#   return answer