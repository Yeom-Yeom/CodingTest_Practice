def rectangle_area(dots):
    x_dot = [dot[0] for dot in dots]
    y_dot = [dot[1] for dot in dots]
    return (max(x_dot)-min(x_dot)) * (max(y_dot)-min(y_dot))

# 다른 사람의 풀이
# def solution(dots):
#   return (max(dots)[0] - min(dots)[0])*(max(dots)[1]-min(dots)[1])