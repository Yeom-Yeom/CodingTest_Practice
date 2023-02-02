def rock_scissor_paper(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer+='0'
        if i == '0':
            answer+='5'
        if i  == '5':
            answer+='2'
    return answer

# 다른 사람의 풀이
# def solution(rsp):
#   d = {'0':'5','2':'0','5':'2'}
#   return ''.join(d[i] for i in rsp)