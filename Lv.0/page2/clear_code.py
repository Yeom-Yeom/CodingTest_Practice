def clear_code(cipher,code):
    answer=''
    for i in range(code-1,len(cipher),code):
        answer+=cipher[i]
    return answer

# 다른 사람의 풀이
# def solution(cipher, code)
#   return cipher[code-1::code]