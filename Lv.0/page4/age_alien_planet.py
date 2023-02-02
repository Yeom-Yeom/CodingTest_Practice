def age_alien_planet(age):
    answer=''
    dic = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}
    for i in str(age):
        answer+=dic[int(i)]
    return answer
# 다른 사람의 풀이
# def solution(age):
#   return ''.join([chr(int(i)+97) for i in str(age)])