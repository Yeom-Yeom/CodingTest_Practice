def ant_corps(hp):
    answer =0
    answer += hp//5
    hp = hp%5
    answer+= hp//3
    hp = hp%3
    answer += hp
    return answer

# 다른 사람의 풀이
# def solution(hp):    
#   return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
   