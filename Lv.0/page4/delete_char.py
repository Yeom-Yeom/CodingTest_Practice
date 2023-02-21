def delete_char(my_string, letter):
    answer = ''
    for i in my_string:
        if i!=letter:
            answer+=i
    return answer

# 다른 사람의 풀이
# def solution(my_string, letter):
#   return my_string.replace(letter,'')