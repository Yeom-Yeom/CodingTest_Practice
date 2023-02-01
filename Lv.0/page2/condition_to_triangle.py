def condition_to_triangle(sides):
    sides = sorted(sides)
    if sides[0]+sides[1] > sides[2]:
        return 1
    else:
        return 2
# 다른 사람의 풀이
# def solution(sides):
#   return 1 if max(sides) < (sum(sides)-max(sides)) else 2