def min_rect(sizes):
    w,h=0,0
    for i in sizes:
        i = sorted(i)
        if w < i[0]:
            w = i[0]
        if h < i[1]:
            h = i[1]
    return w*h

# another solution
# def solution(sizes):
#   return max(max(x) for x i n sizes) * max(min(x)for x in sizes)