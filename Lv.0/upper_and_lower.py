def upper_and_lower(my_string):
    answer=''
    for i in my_string:
        if i.isupper(): # 대문자라면
            answer+=i.lower() # 소문자로 치환
        else: #소문자라면
            answer+=i.upper() # 대문자로 치환
    return answer

# 다른 사람 풀이
# def solution(my_string):
#   return my_string.swapcase()