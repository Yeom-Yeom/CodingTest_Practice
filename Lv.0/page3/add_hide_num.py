import re # findall() 함수를 사용하기 위한 import re
def add_hide_num(my_string):
    answer = re.findall(r"[0-9]+",my_string) # my_string에 0부터 9까지의 숫자가 있는 지 찾기.
    result = 0
    for i in answer:
        result+=int(i)
    return result

# 다른 사람의 풀이
# def solution(my_string):
#   s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#   return sum(int(i) for i in s.split())