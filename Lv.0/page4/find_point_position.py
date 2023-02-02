def find_point_position(dot):
    if dot[0]>0 and dot[1]>0:
        return 1
    elif dot[0]<0 and dot[1]>0:
        return 2
    elif dot[0]<0 and dot[1]<0:
        return 3
    else:
        return 4

# 다른 사람의 풀이
# def solution(dot):
#   quad = [(3,2),(4,1)]
#   return quad[dot[0]>0][dot[1]>0]