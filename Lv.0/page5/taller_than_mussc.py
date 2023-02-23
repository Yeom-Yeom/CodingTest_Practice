def taller_than_mussc(array,height):
    answer=0
    for i in array:
        if height < i:
            answer+=1
    return answer

# 다른 사람의 풀이
# def solution(array,height):
#   return sum(1 for a in array if a>height)